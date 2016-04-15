#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BobTodd'
SITENAME = 'Perfectly Cromulent'
SITEURL = ''

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My personal configuration options

# cf. Notions and Notes
#   http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html
# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['extract_toc','render_math','disqus_static','better_figures_and_images']
# MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

THEME = 'themes/built-texts'

COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = "Mainly...."