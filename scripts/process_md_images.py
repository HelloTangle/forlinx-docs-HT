import os
import re
import sys
import requests
import shutil
from pathlib import Path
from urllib.parse import urlparse
import time

# ==========================================
# 🌟 核心配置区
# ==========================================

ROOT_DIR = Path('.')
# 统一打包的临时收件箱，给 GitHub Actions 稍后上传使用
TEMP_UPLOAD_DIR = Path('./_temp_upload') 
# 飞凌官网后台服务器对外公开访问的图片 URL 前缀
SERVER_BASE_URL = "https://www.forlinx.net/docs_assets/images" 

# 改进的正则匹配：支持带尖括号 <...>、title 以及含空格的路径
IMG_REGEX = re.compile(r'!\[.*?\]\(\s*<?(?P<url>[^)\s]+(?:\s[^)]*)?)>?\s*\)')

# ==========================================
# 🛠️ 核心功能函数区
# ==========================================

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
    
    # 🌟 1. 方案B核心：直接获取 MD 文件在项目里的原生相对路径
    relative_dir = md_path.parent 
    
    # 🌟 2. 建立 1:1 的原生镜像物理目录
    target_dir = (TEMP_UPLOAD_DIR / relative_dir / md_name).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"📦 目标存储结构: {relative_dir} / {md_name}")

    def repl(match):
        img_url = match.group('url').strip()
        img_name = get_clean_filename(img_url)
        save_path = target_dir / img_name
        
        # 将 Windows 的反斜杠 \ 转换为 URL 标准的正斜杠 /
        url_path = str(relative_dir).replace('\\', '/')
        # 计算出这幅图在 1:1 镜像下【理应具备的最完美 URL】
        perfect_server_url = f"{SERVER_BASE_URL}/{url_path}/{md_name}/{img_name}"

        # 🌟 3. 升级版智能锁：不仅要看域名，还要看路径对不对！
        if img_url == perfect_server_url:
            # 只有当目前的链接和最完美的 1:1 链接一模一样时，才真正跳过
            return match.group(0)

        # 🌟 4. 安全落地机制：发现是旧链接、外链或本地图，统统重新抓取！
        if img_url.startswith(('http://', 'https://')):
            # 如果是官网的老路径图，脚本会把它重新下载回来，放进新的 1:1 目录备用
            success = download_image(img_url, save_path)
        else:
            abs_path = (md_path.parent / img_url).resolve() if not os.path.isabs(img_url) else Path(img_url)
            if abs_path.exists():
                success = copy_local_image(abs_path, save_path)
            else:
                print(f"⚠️ 物理文件丢失: {img_url}")
                success = False

        # 🌟 5. 源码改写机制：直接替换为最完美的原生路径
        if success:
            return f"![Image]({perfect_server_url})"
        else:
            return match.group(0)

    # 执行替换并写回文件
    new_content = IMG_REGEX.sub(repl, content)
    md_path.write_text(new_content, encoding='utf-8')
    print("✅ 该文件处理完毕，云端原生链接已更新！")

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

    print(f"🔎 启动 1:1 镜像原生图床分离流水线，共 {len(md_files)} 个任务...")
    for md in md_files:
        try:
            process_md_file(md)
        except Exception as e:
            print(f"❌ 严重崩溃 {md} : {e}")

if __name__ == "__main__":
    main()