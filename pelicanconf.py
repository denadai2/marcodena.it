#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marco De Nadai'
SITENAME = u'Marco De Nadai'
#SITEURL = 'http://www.marcodena.it'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_PATHS = ['pages', 'projects']

PLUGIN_PATHS = ["plugins", "/srv/pelican/plugins"]
PLUGINS = [
    'share_post',
    'sitemap'
]

THEME = 'theme'

STATIC_PATHS = [
    'extra/robots.txt',
    'extra/CV.pdf',
    'images/'
    ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CV.pdf': {'path': 'CV.pdf'},
    }

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = ('index', 'blog',)
