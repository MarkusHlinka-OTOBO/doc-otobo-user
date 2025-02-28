#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Variables ------------------------------------------------------------
# See: https://stackoverflow.com/a/36331678
doc_datestamp = '2024-08-29'
doc_description = 'This is the description of the documentation.'
doc_license = 'GNU Free Documentation License'
doc_name = 'OTOBO User Manual'
doc_url = 'https://otobo.org'
doc_vendor = 'Rother OSS GmbH'
doc_version = '11.0'
doc_yearstamp = '2024'

rst_prolog = """
.. |doc-datestamp| replace:: {0}
.. |doc-description| replace:: {1}
.. |doc-license| replace:: {2}
.. |doc-name| replace:: {3}
.. |doc-url| replace:: {4}
.. |doc-vendor| replace:: {5}
.. |doc-version| replace:: {6}
.. |doc-yearstamp| replace:: {7}
""".format(
doc_datestamp,
doc_description,
doc_license,
doc_name,
doc_url,
doc_vendor,
doc_version,
doc_yearstamp,
)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks'
]

extlinks = {
    'sysconfig': (
        'https://doc.otobo.org/doc/manual/config-reference/11.0/en/content/%s',
        ''
    )
}

# Add any paths that contain templates here, relative to this directory.
# Allow for overriding the RTD theme templates from our own directory.
templates_path = ['/opt/otrs/var/thirdparty/_sphinx-themes/sphinx_rtd_theme/otrs-templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'content/index'

# General information about the project.
project = 'OTOBO User Manual'
copyright = '2019-2024 Rother OSS GmbH, https://otobo.de/'
author = 'Rother OSS GmbH'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '11.0'
# The full version, including alpha/beta/rc tags.
release = '11.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Options for localization
locale_dirs = ['locale/']
gettext_compact = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_logo = '/opt/otrs/var/thirdparty/_static/images/otobo-logo.png'
html_theme_path = ['/opt/otrs/var/thirdparty/_sphinx-themes']
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['/opt/otrs/var/thirdparty/_static']
html_style = 'css/otobo.css'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# do not add the source folder to the html output
html_copy_source = False

html_context = {
    "display_github": True,
    "github_user": "RotherOSS",
    "github_repo": "doc-otobo-doc-otobo-user",
    "github_version": "master",
    "conf_py_path": "/",
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'doc-otobo-doc-otobo-user'


# -- Options for LaTeX output ---------------------------------------------

latex_logo = '/opt/otrs/var/thirdparty/_static/images/otobo-logo.png'

latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional options for the LaTeX preamble.
    #
    # Set postscript to ucs, usage of utf8 and font familiy to helvetica
    'preamble': '''
\usepackage{ucs}
\usepackage[utf8x]{inputenc}
\usepackage{tgtermes}
\usepackage{tgheros}
\usepackage{tgcursor}
\setmonofont{TeX Gyre Cursor}
\setmainfont{Quicksand}
\setsansfont{Quicksand}
''',

# TODO: beautify the whole thing - suggestions:
#% use the Quicksand font instead of TeX Gyre Heros (has to be installed; e.g. present in /usr/share/fonts/truetype/quicksand/)
#\setmainfont{Quicksand}
#\setsansfont{Quicksand}
#% for package docs the "Chapter" style is a bit much; instead of usepackage[Sonny]{fncychap} try overwriting this sphinx-default(?) by adding
#\usepackage{titlesec}
#\titleformat{\chapter}[hang]{\Huge\bfseries}{\thechapter}{0.8em}{\Huge\bfseries}

#\usepackage[fallback]{xeCJK}
# Rother OSS / TODO: Do not need vietnam chars, bug
# \setCJKmainfont{HAN NOM A}
# \setCJKfallbackfamilyfont{rm}{HAN NOM B}
# EO Rother OSS
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'doc-otobo-doc-otobo-user.tex', 'OTOBO User Manual',
     'Rother OSS GmbH', 'manual'),
]

# -- Options for EPUB output ----------------------------------------------

# Supress "unknown mimetype for ..." warnings
suppress_warnings = ['epub.unknown_project_files']

epub_author = u'Rother OSS GmbH'
epub_publisher = u'Rother OSS GmbH'
epub_cover = ('/opt/otrs/var/thirdparty/_static/images/otobo-logo.png', '')
epub_show_urls = 'no'

