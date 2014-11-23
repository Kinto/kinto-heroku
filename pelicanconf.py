#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = os.environ.get('PELICAN_AUTHOR')
SITENAME = os.environ.get('PELICAN_SITENAME', 'Pelican')
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = int(os.environ.get('DEFAULT_PAGINATION', 10))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
