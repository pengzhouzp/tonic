import tonic

project = "Tonic"
copyright = "2019-2021, the neuromorphs of Telluride"
author = "Gregor Lenz"

master_doc = "index"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "pbr.sphinxext", "myst_nb"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# MyST settings
jupyter_execute_notebooks = "off"
suppress_warnings = ["myst.header"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = tonic.__version__
html_logo = "_static/tonic-logo-black.png"
html_favicon = "_static/tonic_favicon.png"
html_show_sourcelink = True
html_sourcelink_suffix = ""

html_theme_options = {
    "repository_url": "https://github.com/neuromorphs/tonic",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "develop",
    "path_to_docs": "docs",
    "use_fullscreen_button": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
