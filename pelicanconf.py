#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = "Cian O'Flynn"
SITENAME = ""
SITETITLE = AUTHOR
SITESUBTITLE = "i-wysiwygcybesurfer2.0" 
SITEDESCRIPTION = "Site description goes here"
# Alter for testing locally 
#SITEURL = "http://localhost:8000"
SITEURL = "https://cianoflynn.github.io"

SITELOGO = SITEURL+"/images/profile.png"
FAVICON = SITEURL+"/images/favicon.ico" 
ROBOTS = "index, follow"


THEME = "Flex"
PATH = "content"
STATIC_PATHS = ["images", "figures"]
ARTICLE_PATHS = ["blog"]
PAGE_PATHS = ["pages"]
TIMEZONE = "Europe/Dublin"
DEFAULT_LANG = "en"


DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (("twitter", 	"https://twitter.com/cianoflynn"),
	     ("github", 	"https://github.com/cianoflynn"),
         ("rss", "https://cianoflynn.github.io/feeds/all.atom.xml"))

MENUITEMS = (("Archives", "/archives.html"),
            ("Categories", "/categories.html"),
	        ("Tags", "/tags.html"),
            ("Atom", "https://cianoflynn.github.io/feeds/all.atom.xml"),
            ("RSS", "https://cianoflynn.github.io/feeds/all.rss.xml"),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "cianoflynn-github-com"
ADD_THIS_ID = 'ra-597a1013e84a12df'
STATUSCAKE = 'rQ8ZHS9lXr'
GOOGLE_ANALYTICS = 'UA-1234-5678'