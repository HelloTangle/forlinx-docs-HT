import os
import shutil

# 公共静态资源目录
COMMON_STATIC_DIR = 'common_static'

# 平台总目录
PLATFORM_ROOT = 'platform'

def copy_static_files(target_dir):
    """复制静态资源到目标平台目录的 _static 文件夹"""
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

def generate_brand_index_rst(brand_dir):
    """生成品牌目录下的 index.rst，列出旗下所有平台目录"""
    index_path = os.path.join(brand_dir, 'index.rst')
    platforms = [d for d in os.listdir(brand_dir)
                 if os.path.isdir(os.path.join(brand_dir, d))]

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

    brands = [d for d in os.listdir(PLATFORM_ROOT)
              if os.path.isdir(os.path.join(PLATFORM_ROOT, d))]

    for brand in brands:
        brand_dir = os.path.join(PLATFORM_ROOT, brand)
        generate_brand_index_rst(brand_dir)

        # 只复制静态资源到平台层（不再生成平台 index.rst）
        platforms = [d for d in os.listdir(brand_dir)
                     if os.path.isdir(os.path.join(brand_dir, d))]
        for platform in platforms:
            platform_dir = os.path.join(brand_dir, platform)
            copy_static_files(platform_dir)

if __name__ == '__main__':
    main()
