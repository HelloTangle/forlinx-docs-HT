import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('.'))

# --- 基础信息：已全部替换为 EmbedSBC ---
project = 'EmbedSBC Documentation'
author = 'EmbedSBC'
copyright = f'{datetime.now().year}, EmbedSBC'

# --- 插件配置 ---
extensions = [
    'myst_parser',
    'sphinx_sitemap',  # 启用 sitemap 生成以配合 SEO
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# --- 主题与 UI 配置 ---
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
    'theme-switcher.css',
]

html_js_files = [
    'theme-switcher.js',
    'logo-link.js',
]

html_logo = '_static/embedsbc-logo.png'
html_favicon = '_static/embedsbc.png'

html_theme_options = {
    'logo_only': True,
    "style_nav_header_background": "#2980B9",
}

html_show_sourcelink = False

# --- SEO 与抓取配置 ---
html_baseurl = 'https://docs.embedsbc.com/'
sitemap_url_scheme = "{link}"

# 注：已删除不支持的 html_sidebars 字典，请通过 _templates/layout.html 覆盖底部