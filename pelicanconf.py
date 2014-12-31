#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['plugins/']
PLUGINS=['sitemap', 'assets',]

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

# Seralization options.
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

THEME = "BT3-Flat"

# These need to be here in order to use the BT3-Flat theme
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blog')
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
POST_LIMIT=10


AUTHOR = 'Alex Lord'
SITENAME = 'My Grown Ass Adult Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Shows up in 'About' Section of home page for BT3-Flat theme.
PERSONAL_INFO = """My name is Alex Lord, a Software Engineer who is working &
living in Seattle, Washington. I started programming in college starting in 
2009 and am one of the (seemingly) rare individuals who didn't start at a 
young age. I'm an amature dancer, writer, food nerd, and lover of many 
things."""

WORK_DESCRIPTION = """I haven't made any major public contributions at this
point in my life. All of my work has been, sadly, behid closed doors."""

WORK_LIST = (
    (
        'link',
        '',
        'Stack OverFlow Profile',
        'Answer questions is hard',
        'https://stackoverflow.com/users/1322962/rawrgulmuffins'),)

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
         ('Personal Twitter Account', 'https://twitter.com/AlexMLord'),)


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
