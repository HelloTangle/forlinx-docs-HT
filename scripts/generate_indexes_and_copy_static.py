import os
import shutil

# 顶层目录和静态资源目录
PLATFORM_DIR = "platform"
STATIC_TEMPLATE_DIR = "common_static"

# 生成顶层 index.rst 文件，列出所有品牌
def write_top_index(brands):
    lines = [
        "Welcome to Forlinx Embedded Documentation",
        "===========================================",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :caption: Brands and Platforms",
        "",
    ]
    for brand in brands:
        lines.append(f"   {brand}/index")
    content = "\n".join(lines)
    with open("index.rst", "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote top-level index.rst")

# 生成品牌目录 index.rst，列出该品牌下所有子平台
def write_brand_index(brand, subplatforms):
    brand_dir = os.path.join(PLATFORM_DIR, brand)
    lines = [
        f"{brand.capitalize()} Platforms",
        "=" * (len(brand) + 10),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ]
    for sp in subplatforms:
        lines.append(f"   {sp}/index")
    content = "\n".join(lines)
    index_path = os.path.join(brand_dir, "index.rst")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {brand}/index.rst")

# 复制 common_static 目录下的静态文件到每个平台 _static 目录
def copy_static_files_to_subplatform(brand, subplatform):
    src_static = STATIC_TEMPLATE_DIR
    dest_static = os.path.join(PLATFORM_DIR, brand, subplatform, "_static")
    os.makedirs(dest_static, exist_ok=True)
    for file_name in os.listdir(src_static):
        full_src = os.path.join(src_static, file_name)
        full_dest = os.path.join(dest_static, file_name)
        shutil.copy2(full_src, full_dest)
    print(f"Copied static files to {dest_static}")

def main():
    if not os.path.exists(PLATFORM_DIR):
        print(f"Error: {PLATFORM_DIR} not found!")
        return
    if not os.path.exists(STATIC_TEMPLATE_DIR):
        print(f"Warning: {STATIC_TEMPLATE_DIR} not found! Static files won't be copied.")

    brands = sorted(
        [d for d in os.listdir(PLATFORM_DIR) if os.path.isdir(os.path.join(PLATFORM_DIR, d))]
    )

    # 生成顶层 index.rst
    write_top_index(brands)

    # 生成每个品牌目录 index.rst，复制静态文件
    for brand in bra
