# -*- coding: utf-8 -*-
#
# wrfout documentation build configuration file, created by
# sphinx-quickstart on Wed May 22 11:34:23 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(dirname(__file__))))

# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
              'sphinx.ext.pngmath']

# Add any paths that contain templates here, relative to this directory.
templates_path = []   # ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'wrfout'
copyright = u'2013, Yagnesh Raghava Yakkala'

# The short X.Y version.
version = '0.1-dev'
# The full version, including alpha/beta/rc tags.
release = '0.1-dev'

exclude_patterns = []

pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'default'

html_static_path = ['_static']
htmlhelp_basename = 'wrfoutdoc'


# -- Options for LaTeX output --------------------------------------------------
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'wrfout.tex', u'wrfout Documentation',
   u'Yagnesh Raghava Yakkala', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'wrfout', u'wrfout Documentation',
     [u'Yagnesh Raghava Yakkala'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'wrfout', u'wrfout Documentation',
   u'Yagnesh Raghava Yakkala', 'wrfout', 'One line description of project.',
   'Miscellaneous'),
]

autodoc_member_order = 'bysource'
autodoc_default_flags = ['members']