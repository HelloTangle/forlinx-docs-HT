import os
import re
import sys
import requests
import shutil
from pathlib import Path
from urllib.parse import urlparse
import time

# ==========================================
# 🌟 核心配置区（全局变量与映射表）
# ==========================================

ROOT_DIR = Path('.')
# 统一打包的临时收件箱，给 GitHub Actions 稍后上传使用
TEMP_UPLOAD_DIR = Path('./_temp_upload') 
# 飞凌官网后台服务器对外公开访问的图片 URL 前缀
SERVER_BASE_URL = "https://www.forlinx.net/docs_assets/images" 

# 🧠 智能分拣字典：在这里维护芯片型号与大平台的映射关系
# 只要文件名或路径里包含以下 key，就会自动分拣到对应的 value 大平台里
CHIP_TO_PLATFORM = {
    "rk3588": "rockchip", 
    "rk3576": "rockchip", 
    "rk3568": "rockchip", 
    "rk3572": "rockchip",
    "imx95": "nxp", 
    "imx8": "nxp", 
    "imx9": "nxp", 
    "ls1046": "nxp",
    "t113": "allwinner", 
    "t507": "allwinner", 
    "a40i": "allwinner",
    "am62x": "ti", 
    "am335x": "ti"
}

# 改进的正则匹配：支持带尖括号 <...>、title 以及含空格的路径
IMG_REGEX = re.compile(r'!\[.*?\]\(\s*<?(?P<url>[^)\s]+(?:\s[^)]*)?)>?\s*\)')

# ==========================================
# 🛠️ 核心功能函数区
# ==========================================

def get_platform_and_chip(md_path: Path) -> tuple:
    """
    智能识别 1级大平台(如rockchip) 和 2级芯片型号(如rk3588)
    """
    path_str = str(md_path).lower()
    parts = md_path.parts

    # 策略 1：如果物理目录本身就非常规范 (例如 platform/rockchip/rk3588/...)
    if 'platform' in parts:
        try:
            idx = parts.index('platform')
            if idx + 1 < len(parts) and idx + 2 < len(parts):
                return parts[idx + 1], parts[idx + 2]
            elif idx + 1 < len(parts):
                return parts[idx + 1], "generic"
        except ValueError:
            pass

    # 策略 2：基于字典的关键词拦截（防呆设计）
    for chip, platform in CHIP_TO_PLATFORM.items():
        if chip in path_str:
            return platform, chip

    # 策略 3：如果实在匹配不到，放入未分类文件夹
    return "others", "generic"

def get_clean_filename(url: str) -> str:
    """提取并清洗图片文件名，确保没有非法字符"""
    path = urlparse(url).path if url.startswith(('http://', 'https://')) else url
    raw_name = os.path.basename(path)
    name_part, ext = os.path.splitext(raw_name)
    ext = ext.lower() if ext.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp'] else '.png'
    # 只保留字母数字下划线，最长 64 个字符，防止文件名过长报错
    safe_name = re.sub(r'[^\w]', '_', name_part)[-64:]
    return safe_name + ext

def download_image(url: str, save_path: Path) -> bool:
    """下载网络图片，自带 3 次重试和超时防卡死机制"""
    if save_path.exists():
        print(f"✅ 已存在 (跳过下载): {save_path.name}")
        return True

    for attempt in range(3):
        try:
            print(f"⬇️ 正在下载: {url}")
            r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            save_path.write_bytes(r.content)
            return True
        except Exception as e:
            print(f"⚠️ 下载失败 ({attempt+1}/3) {url}: {e}")
            time.sleep(5)
    return False

def copy_local_image(src_path: Path, save_path: Path) -> bool:
    """将本地图片提取并复制到临时打包目录"""
    try:
        if save_path.exists():
            print(f"✅ 已存在 (跳过提取): {save_path.name}")
            return True
        shutil.copy2(src_path, save_path)
        print(f"📂 已提取到打包目录: {save_path.name}")
        return True
    except Exception as e:
        print(f"❌ 复制失败 {src_path}: {e}")
        return False

# ==========================================
# 🚀 业务执行主逻辑
# ==========================================

def process_md_file(md_path: Path):
    """处理单个 Markdown 文件的完整生命周期"""
    print(f"\n📄 正在分析: {md_path}")
    if not md_path.exists():
        print(f"⚠️ 文件不存在: {md_path}")
        return

    content = md_path.read_text(encoding='utf-8')
    matches = list(re.finditer(IMG_REGEX, content))
    if not matches:
        print("🔍 未发现任何图片引用，跳过。")
        return

    md_name = md_path.stem
    
    # 🌟 1. 智能提取 4 层架构所需的路径节点
    platform_name, chip_name = get_platform_and_chip(md_path)
    
    # 🌟 2. 建立标准的 4 层物理目录
    # 结构：_temp_upload / 大平台(rockchip) / 芯片(rk3588) / 文档名(hardware_manual) /
    target_dir = (TEMP_UPLOAD_DIR / platform_name / chip_name / md_name).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"📦 目标存储结构: {platform_name} / {chip_name} / {md_name}")

    def repl(match):
        img_url = match.group('url').strip()
        
        # 🌟 3. 防重复处理锁：如果已经是新服务器的链接，原样返回，不折腾
        if img_url.startswith(SERVER_BASE_URL):
            return match.group(0)

        img_name = get_clean_filename(img_url)
        save_path = target_dir / img_name

        # 🌟 4. 安全落地机制：先抓图片
        if img_url.startswith(('http://', 'https://')):
            success = download_image(img_url, save_path)
        else:
            # 处理相对路径或绝对路径
            abs_path = (md_path.parent / img_url).resolve() if not os.path.isabs(img_url) else Path(img_url)
            if abs_path.exists():
                success = copy_local_image(abs_path, save_path)
            else:
                print(f"⚠️ 物理文件丢失: {img_url}")
                success = False

        # 🌟 5. 源码改写机制：确认图片落地安全后，再替换代码
        if success:
            server_url = f"{SERVER_BASE_URL}/{platform_name}/{chip_name}/{md_name}/{img_name}"
            return f"![Image]({server_url})"
        else:
            # 如果图片获取失败，保留原始 MD 代码，防止搞出“裂图”
            return match.group(0)

    # 执行替换并写回文件
    new_content = IMG_REGEX.sub(repl, content)
    md_path.write_text(new_content, encoding='utf-8')
    print("✅ 该文件处理完毕，云端链接已更新！")

def main():
    md_files = []
    
    # 支持命令行参数传入特定文件，方便 GitHub Actions 增量调用
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            path = Path(arg.strip())
            if path.exists() and path.suffix == '.md':
                md_files.append(path)
            else:
                print(f"⚠️ 忽略非 Markdown 文件: {arg}")
    else:
        # 默认全量扫描当前目录下所有的 .md 文件
        md_files = list(ROOT_DIR.rglob('*.md'))

    if not md_files:
        print("🔹 当前路径下未找到需要处理的 Markdown 文件")
        return

    print(f"🔎 启动自动化图床分离流水线，共 {len(md_files)} 个任务...")
    for md in md_files:
        try:
            process_md_file(md)
        except Exception as e:
            print(f"❌ 严重崩溃 {md} : {e}")

if __name__ == "__main__":
    main()