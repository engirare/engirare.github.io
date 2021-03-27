#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'engirare'
SITENAME = u'Blog de EngiRare'

SITESUBTITLE = 'Notas de una ingeniera rara <br> aprendiendo'
#SITEURL = ''
BROWSER_COLOR = "#31C0AF"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

PATH = 'content'
OUTPUT_PATH = './../'

TIMEZONE = 'America/Mexico_City'


DEFAULT_LANG = u'es'

#ARCHIVES_SAVE_AS = ''
#AUTHOR_SAVE_AS = ''
#AUTHORS_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
#CATEGORIES_SAVE_AS = ''
#TAGS_SAVE_AS = ''


THEME = u'Flex'




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),)

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

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

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
