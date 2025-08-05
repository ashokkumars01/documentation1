extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_multiversion"
]

templates_path = ['_templates']

html_context = {
    'display_github': True,
}

smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^master$'
smv_latest_version = 'master'
