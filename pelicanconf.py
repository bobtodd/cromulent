#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BobTodd'
SITENAME = 'Perfectly Cromulent'
SITEURL = ''
# SITEURL = 'localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LRC', 'http://www.utexas.edu/cola/centers/lrc/'),
		)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/bobtodd'),
          ('Twitter', 'https://twitter.com/toddbkrause'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



# My personal configuration options

# cf. Notions and Notes
#   http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','render_math','disqus_static','better_figures_and_images']
# MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

# From Tips-n-Tricks here:
#  https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
MD_EXTENSIONS = [
    CodeHiliteExtension(css_class='highlight'),
    TocExtension(permalink=True),
    'markdown.extensions.extra',
]

# cf. Notions and Notes GitHub repository
#   https://github.com/notionsandnotes/notionsandnotes.org/blob/master/pelican/pelicanconf.py
TYPOGRIFY = True

# The 'elegant' theme automatically includes the Table of Contents
# in the sidebar.  For other themes, you need to add
# {% if article.toc %}
#     <nav class="toc">
#     {{ article.toc }}
#     </nav>
# {% endif %}
# as mentioned here
#   https://github.com/getpelican/pelican-plugins/tree/master/extract_toc
THEME = 'themes/elegant'

COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = "Mainly...."

# DISQUS_SITENAME = "perfectly-cromulent.disqus.com"
DISQUS_SITENAME = "perfectly-cromulent"