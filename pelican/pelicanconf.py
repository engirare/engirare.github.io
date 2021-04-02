#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'engirare'
SITENAME = u'Blog de EngiRare'


BIO = 'Notas de una ingeniera rara <br> ¡Aprende conmigo!'
#SITEURL = ''



PATH = 'content'
OUTPUT_PATH = './../'

TIMEZONE = 'America/Mexico_City'


DEFAULT_LANG = u'es'



THEME = u'pelican-hyde-spanish-local'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),)

USE_FOLDER_AS_CATEGORY = False
#MAIN_MENU = True
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (
    ("Archivo", "/archives.html"),
    ("Categorías", "/categories.html"),
    ("Tags", "/tags.html"),
)
COLOR_THEME= '0c'


FOOTER_TEXT = 'Creative Commons Attribution-ShareAlike 4.0 International License'

#datetime.now().year + 
# Social widget
SOCIAL = (('twitter', 'https://twitter.com/engirare'),
          ('github', 'https://github.com/engirare'),
          ('instagram', 'https://www.instagram.com/engi.rare/'),
          ('envelope', 'engirare@tutanota.com'),)



# Menu

DEFAULT_PAGINATION = 7

TYPOGRIFY = True

STATIC_PATHS = ['images']
PROFILE_IMAGE = 'logo.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
