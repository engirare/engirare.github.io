#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'engirare'
SITENAME = u'Blog de EngiRare'

BIO = 'Notas de una ingeniera rara <br> aprendiendo'
#SITEURL = ''



PATH = 'content'
OUTPUT_PATH = './../'

TIMEZONE = 'America/Mexico_City'


DEFAULT_LANG = u'es'



THEME = u'pelican-hyde'



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
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
COLOR_THEME= '0c'

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "es",
}

COPYRIGHT_YEAR = datetime.now().year

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/engirare'),
          ('GitHub', 'https://github.com/engirare'),
          ('Instagram', 'https://www.instagram.com/engi.rare/'),)



# Menu

DEFAULT_PAGINATION = 7

TYPOGRIFY = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
