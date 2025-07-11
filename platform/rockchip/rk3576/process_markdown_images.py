import os
import re
import requests
from pathlib import Path

# ====== 配置区 ======
ROOT_DIR = Path('.')           # 要遍历的起始路径
IMAGES_ROOT = 'images'         # 所有图片都放这里
IMG_URL_PATTERNS = [
    r'https://cdn\.nlark\.com/[^\s)]+',
    r'https://i\.imgur\.com/[^\s)]+',
    r'https://raw\.githubusercontent\.com/[^\s)]+',
    r'https://s2\.luogu\.com\.cn/[^\s)]+',
    r'https://sm\.ms/[^\s)]+',
]  # 你可以根据需要继续扩展
BACKUP = True                  # 是否保留原 .md 文件备份（.bak）
# ======================

def build_regex():
    patterns = '|'.join(f'({p})' for p in IMG_URL_PATTERNS)
    return re.compile(rf'!\[.*?\]\((?P<url>{patterns})\)')

IMG_REGEX = build_regex()

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
    print(f"\n📄 Processing {md_path.relative_to(ROOT_DIR)}")
    content = md_path.read_text(encoding='utf-8')
    matches = list(re.finditer(IMG_REGEX, content))
    if not matches:
        print("🔍 No images found.")
        return

    # 每个 Markdown 对应一个子目录
    doc_key = md_path.stem  # e.g. hardware_manual
    target_dir = md_path.parent / IMAGES_ROOT / doc_key
    target_dir.mkdir(parents=True, exist_ok=True)

    def repl(match):
        url = match.group('url')
        filename = url.split('/')[-1].split('?')[0]
        shortname = re.sub(r'[^\w]', '', filename)[-32:]
        local_filename = shortname if shortname.endswith('.png') else shortname + '.png'
        local_path = target_dir / local_filename

        success = download_image(url, local_path)
        if success:
            rel_path = f'./{IMAGES_ROOT}/{doc_key}/{local_filename}'
            return f"![Image]({rel_path})"
        else:
            return match.group(0)

    new_content = IMG_REGEX.sub(repl, content)

    if BACKUP:
        backup_path = md_path.with_suffix(md_path.suffix + '.bak')
        backup_path.write_text(content, encoding='utf-8')

    md_path.write_text(new_content, encoding='utf-8')
    print("✅ Saved with local image paths.")

def main():
    md_files = list(ROOT_DIR.rglob('*.md'))
    print(f"🔎 Found {len(md_files)} Markdown files under {ROOT_DIR}")
    for md in md_files:
        process_md_file(md)

if __name__ == "__main__":
    main()
