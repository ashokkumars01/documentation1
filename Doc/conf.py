# conf.py

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# project = 'Your Project'
# author = 'Your Name'
# release = '1.0.0'

# extensions = [
#     'sphinx_multiversion',
#     'myst_parser',  # only if you use Markdown files
#     'sphinx.ext.autodoc'
# ]

# html_theme = "sphinx_rtd_theme"
# html_context = {
#     'display_github': True,
# }
# templates_path = ['Doc/_templates', 'Doc/_static']
# html_js_files = ['versions-menu.js']
# exclude_patterns = []

# html_theme = 'sphinx_rtd_theme'  # or 'furo', etc.

# smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'    # build tags like v1.0.0
# smv_branch_whitelist = r'^master$'          # build only master branch for latest
# smv_latest_version = 'master'                # treat master branch as latest
# smv_rename_latest_version = 'latest'

# html_sidebars = {
#     '**': [
#         'layout.html',
#         'version-switch.html',
#         'globaltoc.html',
#         'relations.html',
#         'searchbox.html',
        
#     ]
# }

# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Your Project'
html_theme = 'alabaster'  # or sphinx_rtd_theme, furo, etc.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_multiversion',
]
templates_path = ['Doc/_templates']

html_static_path = ['_static']
html_css_files = ['version_switch.css']

# sphinx-multiversion config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'  # Only tags like v1.0.0
smv_branch_whitelist = r'^master$'        # Only build from `main`
smv_remote_whitelist = r'^origin$'      # Only from origin
smv_latest_version = 'latest'
smv_rename_latest_version = True

html_theme = 'sphinx_rtd_theme'
html_sidebars = {
    '**': [
        'layout.html',
        'searchbox.html'
    ]
}

# Where to store versions.json
html_context = {
    'display_github': True,
    'versions_json_url': '/versions.json'
}
