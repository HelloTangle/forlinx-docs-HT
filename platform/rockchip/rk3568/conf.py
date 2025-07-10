# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'ROCKCHIP RK3568 Documentation'
author = 'Forlinx Embedded'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',         # 支持 Markdown
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# Logo (如果有，放在 _static 目录)
html_logo = '_static/logo.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
