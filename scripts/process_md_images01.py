import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse

# ====== 配置区 ======
ROOT_DIR = Path('.')           # 要遍历的起始路径
IMAGES_ROOT = 'images'         # 所有图片存放在 ./images/

# 支持的图床 URL 正则（可拓展）
IMG_URL_PATTERNS = [
    r'https://cdn\.nlark\.com/[^\s)]+',
    r'https://i\.imgur\.com/[^\s)]+',
    r'https://raw\.githubusercontent\.com/[^\s)]+',
    r'https://s2\.luogu\.com\.cn/[^\s)]+',
    r'https://sm\.ms/[^\s)]+',
]

# ======================


def build_regex():
    patterns = '|'.join(f'({p})' for p in IMG_URL_PATTERNS)
    return re.compile(rf'!\[.*?\]\((?P<url>{patterns})\)')


IMG_REGEX = build_regex()


def get_clean_filename(url: str):
    """从 URL 中提取干净、合法的文件名"""
    path = urlparse(url).path
    raw_name = os.path.basename(path)
    name_part, ext = os.path.splitext(raw_name)
    ext = ext.lower()
    if ext not in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        ext = '.png'  # fallback 默认使用 .png
    safe_name = re.sub(r'[^\w]', '', name_part)[-32:]  # 截取后32位字符作为安全名称
    return safe_name + ext


def download_image(url: str, save_path: Path):
    if save_path.exists():
        print(f"✅ Already exists: {save_path.name}")
        return True
    try:
        print(f"⬇️  Downloading {url}")
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(r.content)
        return True
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        return False


def process_md_file(md_path: Path):
    print(f"\n📄 Processing {md_path.relative_to(ROOT_DIR)}")
    content = md_path.read_text(encoding='utf-8')
    matches = list(re.finditer(IMG_REGEX, content))
    if not matches:
        print("🔍 No images found.")
        return

    doc_key = md_path.stem
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
    md_files = list(ROOT_DIR.rglob('*.md'))
    print(f"🔎 Found {len(md_files)} Markdown files under {ROOT_DIR}")
    for md in md_files:
        process_md_file(md)


if __name__ == "__main__":
    main()
