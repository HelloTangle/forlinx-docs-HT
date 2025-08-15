import os
import re
import sys
import requests
import shutil
from pathlib import Path
from urllib.parse import urlparse
import time

ROOT_DIR = Path('.')
IMAGES_DIR_NAME = 'images'

# 改进正则：支持 <...>、title、空格路径
IMG_REGEX = re.compile(r'!\[.*?\]\(\s*<?(?P<url>[^)\s]+(?:\s[^)]*)?)>?\s*\)')

def get_clean_filename(url: str):
    """提取安全文件名"""
    path = urlparse(url).path if url.startswith(('http://', 'https://')) else url
    raw_name = os.path.basename(path)
    name_part, ext = os.path.splitext(raw_name)
    ext = ext.lower() if ext.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp'] else '.png'
    safe_name = re.sub(r'[^\w]', '_', name_part)[-64:]
    return safe_name + ext

def download_image(url: str, save_path: Path):
    """下载网络图片，带重试"""
    if save_path.exists():
        print(f"✅ 已存在: {save_path}")
        return True

    for attempt in range(3):
        try:
            print(f"⬇️ 下载 {url} -> {save_path}")
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                f.write(r.content)
            return True
        except Exception as e:
            print(f"⚠️ 下载失败 ({attempt+1}/3) {url}: {e}")
            time.sleep(5)
    return False

def copy_local_image(src_path: Path, save_path: Path):
    """复制本地图片"""
    try:
        if save_path.exists():
            print(f"✅ 已存在: {save_path}")
            return True
        shutil.copy2(src_path, save_path)
        print(f"📂 已复制: {src_path} -> {save_path}")
        return True
    except Exception as e:
        print(f"❌ 复制失败 {src_path}: {e}")
        return False

def process_md_file(md_path: Path):
    print(f"\n📄 处理文件: {md_path}")
    if not md_path.exists():
        print(f"⚠️ 文件不存在: {md_path}")
        return

    content = md_path.read_text(encoding='utf-8')
    matches = list(re.finditer(IMG_REGEX, content))
    if not matches:
        print("🔍 未找到图片引用")
        return

    md_name = md_path.stem
    target_dir = md_path.parent / IMAGES_DIR_NAME / md_name
    target_dir.mkdir(parents=True, exist_ok=True)

    def repl(match):
        img_url = match.group('url').strip()
        img_name = get_clean_filename(img_url)
        save_path = target_dir / img_name

        # 网络图片
        if img_url.startswith(('http://', 'https://')):
            success = download_image(img_url, save_path)
        else:
            # 本地图片
            abs_path = (md_path.parent / img_url).resolve() if not os.path.isabs(img_url) else Path(img_url)
            if abs_path.exists():
                success = copy_local_image(abs_path, save_path)
            else:
                print(f"⚠️ 找不到图片: {img_url}")
                success = False

        if success:
            # 替换为仓库相对路径
            rel_path = f"./{IMAGES_DIR_NAME}/{md_name}/{img_name}"
            return f"![Image]({rel_path})"
        else:
            return match.group(0)

    new_content = IMG_REGEX.sub(repl, content)
    md_path.write_text(new_content, encoding='utf-8')
    print("✅ 已保存并更新图片路径")

def main():
    # 如果传了参数，则按参数文件列表处理
    if len(sys.argv) > 1:
        md_files = []
        for arg in sys.argv[1:]:
            path = Path(arg.strip())
            if path.exists() and path.suffix == '.md':
                md_files.append(path)
            else:
                print(f"⚠️ 参数不是有效 Markdown 文件: {arg}")
    else:
        # 没传参数则扫描整个仓库
        md_files = list(ROOT_DIR.rglob('*.md'))

    print(f"🔎 共找到 {len(md_files)} 个 Markdown 文件")
    for md in md_files:
        process_md_file(md)

if __name__ == "__main__":
    main()
