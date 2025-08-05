# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Your Project'
author = 'Your Name'
release = '1.0.0'

extensions = [
    'sphinx_multiversion',
    'myst_parser',  # only if you use Markdown files
]
html_theme = "sphinx_rtd_theme"
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'  # or 'furo', etc.

smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'    # build tags like v1.0.0
smv_branch_whitelist = r'^master$'          # build only master branch for latest
smv_latest_version = 'master'                # treat master branch as latest
smv_rename_latest_version = 'latest'

html_sidebars = {
    '**': [
        'version-switch.html',
        'globaltoc.html',
        'relations.html',
        'searchbox.html',
    ]
}
