extensions = [
    'sphinx_multiversion',
    'myst_parser',  # only if you're using Markdown (.md) files
    ...
]

templates_path = ['_templates']

html_context = {
    'display_github': True,
}

smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^master$'
smv_latest_version = 'main'
