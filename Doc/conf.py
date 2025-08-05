import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Your Project Name'
author = 'Your Name'
release = 'x.x.x'  # Match this with git tag

extensions = [
    'myst_parser',              # for Markdown
    'sphinx_rtd_theme',         # for nice layout
    'sphinx_multiversion',      # for versioned docs
]
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
master_doc = 'index'
# Versioning Config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^master$'
smv_remote_whitelist = r'^origin$'
smv_released_pattern = r'^tags/v\d+\.\d+\.\d+$'

html_context = {
    'display_github': True,
    'versions': [],
}

templates_path = ['_templates']

html_sidebars = {
    '**': [
        'version-switch.html',   # ← Add this line
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ],
}
