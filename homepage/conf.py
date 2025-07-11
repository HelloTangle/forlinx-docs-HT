import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Forlinx Embedded Documentation'
author = 'Forlinx Embedded'
copyright = 'Forlinx Embedded'

extensions = [
    'myst_parser',  # 支持 Markdown
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

# Logo 文件放在 _static 文件夹，确保路径正确
html_logo = '_static/forlinx-logo.png'
html_favicon = '_static/forlinx.png'

# 主题选项，根据需要调整
html_theme_options = {
    'logo_only': True,

}

html_theme_options = {
    'collapse_navigation': False,   # ❗不折叠，默认全部展开
    'navigation_depth': 4,          # 展示的目录层级，建议设为 2~4
    'titles_only': False,           # 显示全部小节标题，不只展示文档标题
}

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
        'footer.html',  # 👈 关键：显式加载我们自定义的 footer 模板
    ]
}
