# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Doxamples'
copyright = '2026, Doxtr Doc'
author = 'Doxtr Doc'

version = '0.0.1'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinxcontrib.bibtex',
    'sphinx_diagrams',
    'sphinxcontrib.drawio',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.openapi',
    'sphinxcontrib.icon',
    'metapensiero.sphinx.d2',
    'sphinxcontrib.xlink',
    'sphinx_needs',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# Configure allowed tags and their display names for xlink directives
xlink_allowed_tags = {
   'rst': ('reStructuredText', 'These are links to reStructuredText documentation.'),
   'diagramming': ('Diagramming', 'These are links to diagramming documentation.'),
}

# -- Latex elements configuration
latex_toplevel_sectioning = "part"

# -- Options for bibtex extension
bibtex_bibfiles = ['references.bib']

######################################
#     sphinx-needs configuration     #
######################################

needs_build_json = True
needs_types = [
    {
        "directive": "dr",
        "title": "Decision Record",
        "prefix": "_DR",  # prefix for auto-generated IDs
        "style": "rectangle", # style for the type in diagrams
        "color": "#BFD8D2", # color for the type in diagrams
    }
]
needs_id_regex = r'^[a-zA-Z0-9_-]+$'  # IDs can only contain letters, numbers, underscores, and hyphens

# Available from sphinx-needs 7.0.0
needs_fields = {
    "xlink": {
        "description": "Documentation link",
        "schema": {
            "type": "string",
        },
        "nullable": True
    },
    "documentation": {
        "description": "Documentation link",
        "schema": {
            "type": "string",
        },
        "nullable": True
    },
    "python-docs": {
        "description": "Python documentation link",
        "schema": {
            "type": "string",
        },
        "nullable": True
    }
}

# This is a custom setting that integrates with the xlink extension, and allows you to specify which xlink fields should be processed by the xlink extension. This is necessary because the xlink extension needs to know which fields contain xlink references, so it can process them correctly.
xlink_needs_string_link_options = [ 'xlink', 'documentation']

#################################
#     Draw.io configuration     #
#################################

# See https://pypi.org/project/sphinxcontrib-drawio/
# Force the extension to strictly run its own background Xvfb setup
drawio_headless = True
drawio_no_sandbox = True
drawio_builder_export_format = {
     "html": "svg",
     "latexpdf": "png",
     "docx": "png"
}
drawio_default_export_scale = 100
drawio_default_transparency = True
# --- END Draw.io CONFIGURATION ---