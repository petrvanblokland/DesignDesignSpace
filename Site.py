#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     site.py
#
import os
import shutil
import webbrowser

from pagebot.publications.publication import Publication
from pagebot.constants import URL_JQUERY
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color, whiteColor, blackColor
from pagebot.toolbox.units import em, pt
from pagebot.elements.web.simplesite.siteelements import *


SITE_NAME = 'DesignDesign.Space' # Also used as logo

MD_PATH = 'Program2019-01-06.md'
EXPORT_PATH = '_export/' + SITE_NAME # Export path for DO_FILE

VERBOSE = False

DO_PDF = 'Pdf' # Save as PDF representation of the site.
DO_FILE = 'File' # Generate website output in _export/SimpleSite and open browser on file index.html
DO_MAMP = 'Mamp' # Generate website in /Applications/Mamp/htdocs/SimpleSite and open a localhost
DO_GIT = 'Git' # Generate website and commit to git (so site is published in git docs folder.
EXPORT_TYPE = DO_MAMP

blueColor = color(rgb='#2A8BB8')

headerBackgroundColor = color(0.9) #whiteColor
heroBackgroundColor = color(0.95)
bannerBackgroundColor = color(0, 1, 0) #whiteColor
navigationBackgroundColor = blackColor
coloredSectionBackgroundColor = blueColor
logoColor = blueColor
logoBackgroundColor = color(1, 1, 0)
coloredSectionColor = color(0.9)
footerBackgroundColor = color(0.8)
footerColor = blackColor

styles = dict(
    body=dict(
        fill=whiteColor,
        ml=9, mr=0, mt=0, mb=0,
        pl=em(3), pr=em(3), pt=em(3), pb=em(3),
        fontSize=pt(12),
        leading=em(1.4),
    ),
    br=dict(leading=em(1.4)
    ),
)
# Page structure, passed to Navigation to build 
PAGES = (
    dict(href='index.html', label='Home'),
    dict(href='program.html', label='Program', pages=(
        dict(href='program-2019.html', label='2019', pages=(            
            dict(href='program-type-design.html', label='Type design'),
            dict(href='program-graphic-design.html', label='Graphic design'),
            dict(href='program-design-spaces.html', label='Design spaces'),
            dict(href='program-design-practice.html', label='Design practice'),
            )
        ),
        dict(href='program-2018.html', label='2018 Review'),
        )
    ),
    dict(href='scales.html', label='Scales', pages=(
        dict(href='scales-preparing-projects-0.html', label='Preparation'),
        dict(href='scales-sketching-100.html', label='Sketching'),
        dict(href='scales-research-200.html', label='Research'),
        dict(href='scales-programming-coding-400.html', label='Programming'),
        dict(href='scales-design-education-700.html', label='Education'),
        dict(href='scales-type-design-1000.html', label='Type design'),
        dict(href='scales-typography-1100.html', label='Typography'),
        dict(href='scales-design-identities-1300.html', label='Identities'),
        dict(href='scales-design-publications-1400.html', label='Publications'),
        )
    ),
    dict(href='about.html', label='About'),
)

def makeNavigation(doc):
    for pages in doc.pages.values():
        for page in pages:  
            name = page.name
            header = page.select('Header')
            navigation = Navigation(parent=header, fill=navigationBackgroundColor, menuInfo=PAGES)

def makeTemplates(doc):

    home = Template('Home')
    
    home.description = 'DesignDesign.Space website is created by PageBot'
    home.keyWords = 'DesignDesignSpace DesignDesignSpace DesignSpace TYPETR PageBot Python Scripting'
    home.viewPort = 'width=device-width, initial-scale=1.0, user-scalable=yes'
    home.style = styles['body']

    header = Header(parent=home, fill=headerBackgroundColor)
    banner = Banner(parent=header, fill=bannerBackgroundColor)
    logo = Logo(parent=banner, textFill=logoColor, fill=logoBackgroundColor, fontSize=pt(40))
    newTextBox(SITE_NAME, parent=logo)
    # Navigation will be added to header, ones the pages are copied from this template

    # First make the home template
    hero = Hero(parent=home, fontSize=em(1.1), fill=heroBackgroundColor)    
    content = Content(parent=home)
    section = ColoredSection(parent=home, fill=coloredSectionBackgroundColor)
    
    # Then make a deep copy of the home template as default template and add some more elements.
    default = home.copy()
    default.name = 'default'
    content = Content(parent=default, cssId='Content2') #  fill=(0.7, 0.7, 0.9)
    
    # Add footers to the two templates
    Footer(parent=home, fill=footerBackgroundColor, textFill=footerColor)
    Footer(parent=default, fill=footerBackgroundColor, textFill=footerColor)
 
    doc.addTemplate('home', home)
    doc.addTemplate('default', default)

def makeSite(styles, viewId):
    site = Site(styles=styles)
    doc = site.newDocument(viewId=viewId, autoPages=0)
    
    view = doc.view
    view.resourcePaths = ('css','fonts','images','js')
    view.jsUrls = (URL_JQUERY, URL_MEDIA, 'js/main.js')
    # SiteView will automatic generate css/style.scss.css from assumed css/style.scss
    view.cssUrls = ('fonts/webfonts.css', 'css/normalize.css', 'css/style-org.css')

    # Make the all pages and elements of the site as empty containers, that then can
    # be selected and filled by the composer, using the galley content.
    makeTemplates(doc)    
    
    # By default, the typesetter produces a single Galley with content and code blocks.    
    t = Typesetter(doc.context)
    galley = t.typesetFile(MD_PATH)
    
    # Create a Composer for this document, then create pages and fill content. 
    composer = Composer(doc)

    # The composer executes the embedded Python code blocks that indicate where content should go.
    # by the HtmlContext. Feedback by the code blocks is added to verbose and errors list
    targets = composer.compose(galley)

    if VERBOSE:
        if targets['verbose']:
            print('Verbose\n', '\n'.join(targets['verbose']))
        # In case there are any errors, show them.
        if targets['errors']:
            print('Errors\n', '\n'.join(targets['errors']))
    
    # Add the navigation, now we know all the pages.
    makeNavigation(doc)

    return doc
    

if EXPORT_TYPE == DO_PDF: # PDF representation of the site
    doc = makeSite(styles=styles, viewId='Page')
    pageView = doc.view
    doc.solve() # Solve all layout and float conditions for pages and elements.
    doc.export(EXPORT_PATH + '.pdf')

elif EXPORT_TYPE == DO_FILE:
    doc = makeSite(styles=styles, viewId='Site')
    siteView = doc.view
    doc.export(EXPORT_PATH)
    openingPage = 'program-2018.html'
    os.system(u'/usr/bin/open "%s/%s"' % (EXPORT_PATH, openingPage))

elif EXPORT_TYPE == DO_MAMP:
    # Internal CSS file may be switched off for development.
    doc = makeSite(styles=styles, viewId='Mamp')
    mampView = doc.view
    MAMP_PATH = '/Applications/MAMP/htdocs/' 
    filePath = MAMP_PATH + SITE_NAME 
    if VERBOSE:
        print('Site path: %s' % filePath)
    if os.path.exists:
        shutil.rmtree(filePath) # Comment this line, if more safety is required. Then manually delete.
    doc.export(filePath)

    if not os.path.exists(filePath):
        print('The local MAMP server application does not exist. Download and install from %s.' % view.MAMP_SHOP_URL)
        os.system(u'/usr/bin/open %s' % view.MAMP_SHOP_URL)
    else:
        #t.doc.export('_export/%s.pdf' % NAME, multiPages=True)
        os.system(u'/usr/bin/open "%s"' % mampView.getUrl(SITE_NAME))

elif EXPORT_TYPE == DO_GIT and False: # Not supported for SimpleSite, only one per repository?
    # Make sure outside always has the right generated CSS
    doc = makeSite(styles=styles, viewId='Git')
    doc.export(EXPORT_PATH)
    # Open the css file in the default editor of your local system.
    os.system('git pull; git add *;git commit -m "Updating website changes.";git pull; git push')
    os.system(u'/usr/bin/open "%s"' % view.getUrl(DOMAIN))

else: # No output view defined
    print('Set EXPORTTYPE to DO_FILE or DO_MAMP or DO_GIT')

