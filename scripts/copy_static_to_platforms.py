import os
import shutil

# 公共静态资源目录
COMMON_STATIC_DIR = 'common_static'

# 平台根目录
PLATFORM_ROOT = 'platform'

def copy_static_files(target_dir):
    """复制静态资源到目标平台的 _static 文件夹"""
    static_dir = os.path.join(target_dir, '_static')
    os.makedirs(static_dir, exist_ok=True)
    for filename in ['custom.css', 'forlinx-logo.png']:
        src = os.path.join(COMMON_STATIC_DIR, filename)
        dst = os.path.join(static_dir, filename)
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f'Copied {filename} → {dst}')
        else:
            print(f'Warning: {filename} not found in {COMMON_STATIC_DIR}')

def main():
    if not os.path.exists(COMMON_STATIC_DIR):
        print(f'Error: common_static directory not found: {COMMON_STATIC_DIR}')
        return

    if not os.path.exists(PLATFORM_ROOT):
        print(f'Error: platform root directory not found: {PLATFORM_ROOT}')
        return

    for brand in os.listdir(PLATFORM_ROOT):
        brand_path = os.path.join(PLATFORM_ROOT, brand)
        if not os.path.isdir(brand_path):
            continue
        for platform in os.listdir(brand_path):
            platform_path = os.path.join(brand_path, platform)
            if os.path.isdir(platform_path):
                copy_static_files(platform_path)

if __name__ == '__main__':
    main()
