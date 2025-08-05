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

# Sphinx-multiversion config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'   # tags like v1.0.0
smv_branch_whitelist = r'^(main|master)$'  # main or master branch
smv_latest_version = 'master'  # what branch/tag to treat as latest
smv_rename_latest_version = 'latest'  # rename 'main' folder to 'latest' in output
