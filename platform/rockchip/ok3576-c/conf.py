# -- Path setup --------------------------------------------------------------

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

# 👇 已全部替换为 EmbedSBC
project = 'EmbedSBC RK3576 Documentation'
author = 'EmbedSBC'
copyright = f'{datetime.now().year}, EmbedSBC'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',         # 支持 Markdown
    'sphinx_sitemap',      # 添加 sitemap 扩展
]

# 👇 关键修改：Sitemap 的绝对路径基准必须是 embedsbc 的域名！
html_baseurl = "https://docs.embedsbc.com/rockchip/ok3576-c/"

# 👇 防止 Sitemap 生成带版本号和语言的错误路径
sitemap_url_scheme = "{link}"

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# 👇 确保调用的是 embedsbc 的 logo
html_logo = '_static/embedsbc-logo.png'
html_favicon = '_static/embedsbc.png'

html_theme_options = {
    'logo_only': True,
}

html_css_files = [
    'theme-switcher.css',
]

# 注意：已删除 html_sidebars 字典，请通过 _templates/layout.html 覆盖底部

html_show_sourcelink = False

html_js_files = [
    'theme-switcher.js',
    'logo-link.js',
]