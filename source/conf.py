from __future__ import annotations

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "Open-BEATBox Documentation"
author = "NERB team"
copyright = "2026, NERB team"
release = "draft"

extensions = [
    "assembly_videos",
    "myst_parser",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "build/assembly-tutorials/README.md",
    "build/assembly-tutorials/modules/README.md",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "furo"
html_title = "Open-BEATBox Documentation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.png"
html_logo = "_static/beatbox-logo.png"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0891b2",
        "color-brand-content": "#0e7490",
    },
    "dark_css_variables": {
        "color-brand-primary": "#67e8f9",
        "color-brand-content": "#67e8f9",
    },
    "source_repository": "https://github.com/Open-BeatBox/Open-BeatBox.github.io/",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
    "tasklist",
]

root_doc = "index"

nitpicky = False

html_context = {
    "display_github": True,
    "github_user": "Open-BeatBox",
    "github_repo": "Open-BeatBox.github.io",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

_static = Path(__file__).parent / "_static"
_static.mkdir(exist_ok=True)
