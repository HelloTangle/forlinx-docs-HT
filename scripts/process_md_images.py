import os
import re
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse

ROOT_DIR = Path('.')
IMAGES_ROOT = 'images'

IMG_URL_PATTERNS = [
    r'https://cdn\.nlark\.com/[^\s)]+',
    r'https://i\.imgur\.com/[^\s)]+',
    r'https://raw\.githubusercontent\.com/[^\s)]+',
    r'https://s2\.luogu\.com\.cn/[^\s)]+',
    r'https://sm\.ms/[^\s)]+',
]

def build_regex():
    patterns = '|'.join(f'({p})' for p in IMG_URL_PATTERNS)
    return re.compile(rf'!\[.*?\]\((?P<url>{patterns})\)')

IMG_REGEX = build_regex()

def get_clean_filename(url: str):
    path = urlparse(url).path
    raw_name = os.path.basename(path)
    name_part, ext = os.path.splitext(raw_name)
    ext = ext.lower()
    if ext not in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        ext = '.png'
    safe_name = re.sub(r'[^\w]', '', name_part)[-32:]
    return safe_name + ext

def download_image(url: str, save_path: Path):
    if save_path.exists():
        print(f"✅ Already exists: {save_path.name}")
        return True
    try:
        print(f"⬇️ Downloading {url}")
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(r.content)
        return True
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        return False

def process_md_file(md_path: Path):
    print(f"\n📄 Processing {md_path}")
    content = md_path.read_text(encoding='utf-8')
    matches = list(re.finditer(IMG_REGEX, content))
    if not matches:
        print("🔍 No images found.")
        return

    doc_key = re.sub(r'[^\w]', '', md_path.stem)
    target_dir = md_path.parent / IMAGES_ROOT / doc_key
    target_dir.mkdir(parents=True, exist_ok=True)

    def repl(match):
        url = match.group('url')
        local_filename = get_clean_filename(url)
        local_path = target_dir / local_filename
        success = download_image(url, local_path)
        if success:
            rel_path = f'./{IMAGES_ROOT}/{doc_key}/{local_filename}'
            return f"![Image]({rel_path})"
        else:
            return match.group(0)

    new_content = IMG_REGEX.sub(repl, content)
    md_path.write_text(new_content, encoding='utf-8')
    print("✅ Saved with local image paths.")

def main():
    if len(sys.argv) > 1:
        # 从文本文件读取需要处理的.md列表
        md_list_file = Path(sys.argv[1])
        if not md_list_file.exists():
            print(f"Error: {md_list_file} not found.")
            sys.exit(1)
        with open(md_list_file, 'r', encoding='utf-8') as f:
            md_files = [ROOT_DIR / line.strip() for line in f if line.strip()]
    else:
        # 没参数则处理全部md文件
        md_files = list(ROOT_DIR.rglob('*.md'))

    print(f"🔎 Processing {len(md_files)} Markdown files")
    for md in md_files:
        if md.exists():
            process_md_file(md)
        else:
            print(f"Warning: {md} does not exist")

if __name__ == "__main__":
    main()
