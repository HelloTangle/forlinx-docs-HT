# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Forlinx Embedded RK3576 Documentation'
author = 'Forlinx Embedded'
copyright = 'Forlinx Embedded'
# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',         # 支持 Markdown
    'sphinx_sitemap',      # 添加 sitemap 扩展
]
html_baseurl = "https://hellotangle.github.io/forlinx-docs-HT/rockchip/ok3576-c/"


templates_path = ['_templates']
exclude_patterns = []

# 加载自定义 JS
html_js_files = [
    'custom.js',  # 合并后的 JS
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# Logo (如果有，放在 _static 目录)
html_logo = '_static/forlinx-logo.png'
html_favicon = '_static/forlinx.png'
html_theme_options = {
    'logo_only': True,
    'collapse_navigation': False,  # 禁止自动折叠，允许多项同时展开
}

html_css_files = [
    'custom.css',
]

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
        'footer.html',  # 👈 关键：显式加载我们自定义的 footer 模板
    ]
}

html_show_sourcelink = False