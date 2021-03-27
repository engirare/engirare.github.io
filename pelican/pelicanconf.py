#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'engirare'
SITENAME = u'Blog de EngiRare'
#SITEURL = ''

PATH = 'content'
OUTPUT_PATH = './../'

TIMEZONE = 'America/Mexico_City'


DEFAULT_LANG = u'es'

ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''


THEME = u'MinimalXY'
# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
#MINIMALXY_START_YEAR = 2009
#MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hola mundo soy EngiRare.'
AUTHOR_DESCRIPTION = u'Quiero salvar el mundo, apoyandome de la ingeniería y enfocandome en los residuos'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://engirare.com'

# Services
#GOOGLE_ANALYTICS = 'UA-12345678-9'
#DISQUS_SITENAME = 'johndoe'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/engirare'),
          ('GitHub', 'https://github.com/engirare'),
          ('Instagram', 'https://www.instagram.com/engi.rare/'),)

# Menu
MENUITEMS = (
    ('Categories', '/' + CATEGORIES_SAVE_AS),
    ('Archive', '/' + ARCHIVES_SAVE_AS),
)

DEFAULT_PAGINATION = 7

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
