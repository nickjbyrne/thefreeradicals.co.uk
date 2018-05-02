#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mike Gibbs'
SITENAME = 'The Free Radicals'
SITEURL = ''

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
PATH = 'content'
ARTICLE_PATHS = ['articles',]
PAGE_PATHS = ['pages',]
MENUITEMS = (
    ('About Us', '/pages/about.html'),
    ('Music & Media', '/pages/music.html'),
    ('Our History', '/pages/history.html'),
    ('FAQ', '/pages/faq.html'),
    ('Gigs Guide', '/pages/gigs.html'),
    ('Contact Us', '/pages/contact.html')
)


TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/thefreeradsfolk'),
          ('Facebook', 'https://www.facebook.com/TheFreeRadicalsFolk'),
          ('Youtube', 'http://www.youtube.com/freeradicalchap')
         ,)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'simple'

PLUGIN_PATHS = 'plugins'
PLUGINS = ['pelican_javascript', 'embed_tweet']
