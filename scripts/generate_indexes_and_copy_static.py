import os
import shutil

# 你的公共静态资源目录（放置 custom.css, forlinx-logo.png 等）
COMMON_STATIC_DIR = 'common_static'

# 你文档根目录下的平台目录
PLATFORM_ROOT = 'platform'

def copy_static_files(target_dir):
    static_dir = os.path.join(target_dir, '_static')
    os.makedirs(static_dir, exist_ok=True)
    for filename in ['custom.css', 'forlinx-logo.png']:
        src = os.path.join(COMMON_STATIC_DIR, filename)
        dst = os.path.join(static_dir, filename)
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f'Copied {filename} to {dst}')
        else:
            print(f'Warning: {filename} not found in {COMMON_STATIC_DIR}')

def generate_platform_index_rst(platform_dir):
    """
    生成平台目录的 index.rst，列出所有 md 和 rst 文件（除 index.rst）。
    """
    index_path = os.path.join(platform_dir, 'index.rst')
    docs = []
    for f in os.listdir(platform_dir):
        full_path = os.path.join(platform_dir, f)
        if os.path.isfile(full_path) and f != 'index.rst' and (f.endswith('.md') or f.endswith('.rst')):
            docs.append(f[:-3])  # 去掉扩展名
    if not docs:
        print(f'No doc files found in {platform_dir}, skipping index.rst generation.')
        return
    title = os.path.basename(platform_dir).upper()
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write('=' * len(title) + '\n\n')
        f.write('.. toctree::\n')
        f.write('   :maxdepth: 2\n\n')
        for doc in sorted(docs):
            f.write(f'   {doc}\n')
    print(f'Generated platform index.rst: {index_path}')
    # 复制静态资源
    copy_static_files(platform_dir)

def generate_brand_index_rst(brand_dir):
    """
    生成品牌目录的 index.rst，列出旗下所有平台子目录
    """
    index_path = os.path.join(brand_dir, 'index.rst')
    platforms = [d for d in os.listdir(brand_dir) if os.path.isdir(os.path.join(brand_dir, d))]
    if not platforms:
        print(f'No platform dirs found in {brand_dir}, skipping brand index.rst.')
        return
    title = os.path.basename(brand_dir).upper()
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write('=' * len(title) + '\n\n')
        f.write('.. toctree::\n')
        f.write('   :maxdepth: 1\n\n')
        for platform in sorted(platforms):
            f.write(f'   {platform}/index\n')
    print(f'Generated brand index.rst: {index_path}')

def main():
    if not os.path.exists(COMMON_STATIC_DIR):
        print(f'Warning: Common static directory {COMMON_STATIC_DIR} does not exist.')
    if not os.path.exists(PLATFORM_ROOT):
        print(f'Error: Platform root directory {PLATFORM_ROOT} does not exist.')
        return

    brands = [d for d in os.listdir(PLATFORM_ROOT) if os.path.isdir(os.path.join(PLATFORM_ROOT, d))]

    for brand in brands:
        brand_dir = os.path.join(PLATFORM_ROOT, brand)
        generate_brand_index_rst(brand_dir)

        # 遍历品牌下的各个平台目录
        platforms = [d for d in os.listdir(brand_dir) if os.path.isdir(os.path.join(brand_dir, d))]
        for platform in platforms:
            platform_dir = os.path.join(brand_dir, platform)
            generate_platform_index_rst(platform_dir)

if __name__ == '__main__':
    main()
