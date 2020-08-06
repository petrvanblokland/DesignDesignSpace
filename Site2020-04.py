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

from pagebot.contexts import getContext
from pagebot.publications.publication import Publication
from pagebot.publications.instagram import InstagramPost
from pagebot.constants import URL_JQUERY, LANGUAGE_EN, InstagramSquare, CENTER
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.elements import *
from pagebot.toolbox.color import color, whiteColor, blackColor, spotColor
from pagebot.toolbox.units import em, pt, px
from pagebot.elements.web.nanosite.siteelements import *

from css.nanostyle_css import cssPy

from pagebot.themes import *
#   BackToTheCity
#   BusinessAsUsual 
#   FairyTales 
#   FreshAndShiny 
#   IntoTheWoods 
#   SeasoningTheDish 
#   SomethingInTheAir 
#   WordlyWise
#   HappyHolidays

DDS_LOGO = spotColor(165)

class DDSTheme(BaseTheme):
    NAME = 'DesignDesign.Space'
    BASE_COLORS = dict(
        base2=color('#ACACB8'),
        base3=DDS_LOGO,
        logo=DDS_LOGO,
    )

theme = DDSTheme('light')

context = getContext('Html')
assert context is not None

SITE_NAME = 'DesignDesign.Space' # Also used as logo

MD_PATHS = [
    'DDS-home.md',
    'DDS-studies.md',
    'DDS-studies-type_design.md',
    'DDS-studies-typography.md',
    'DDS-studies-graphic_design.md',
    'DDS-studies-spaces.md',
    'DDS-studies-design_practice.md',
    'DDS-studies-design_education.md',
    'DDS-scales.md',
    'DDS-scales-preparing_projects.md',
    'DDS-scales-sketching.md',
    'DDS-scales-programming_coding.md',
    'DDS-scales-design_education.md',
    'DDS-reviews.md',
    'DDS-pricing.md',
    'DDS-contact.md',
]
EXPORT_PATH = '_export/' + SITE_NAME # Export path for DO_FILE
INSTAGRAM_PATH = '_export/Instagram.jpg'

VERBOSE = False

DO_PDF = 'Pdf' # Save as PDF representation of the site.
DO_FILE = 'File' # Generate website output in _export/SimpleSite and open browser on file index.html
DO_MAMP = 'Mamp' # Generate website in /Applications/Mamp/htdocs/SimpleSite and open a localhost
DO_GIT = 'Git' # Generate website and commit to git (so site is published in git docs folder.
DO_TWITTER = 'Twitter' # Generate banners for each workshop on optimal Twitter size.
DO_INSTAGRAM = 'Instagram' # Generate banners for each workshop on optimal Instagram square size.
#EXPORT_TYPES = [DO_GIT]
EXPORT_TYPES = [DO_MAMP, DO_GIT]
#EXPORT_TYPES = [DO_MAMP]
#EXPORT_TYPES = [DO_INSTAGRAM]

CLEAR_MAMP = False # If True, make a clean copy by removing all old files first.

NUM_CONTENT = 2 # Number of content elements on a page.
NUM_SIDES = 1 # Number of side elements next to a main content element,

# Max image size of scaled cache (used mulitplied by resolution per image type DEFAULT_RESOLUTION_FACTORS
MAX_IMAGE_WIDTH = pt(800) 


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

def makeNavigation(doc):
    """After all pages of the site are generated, we can use the compiled page tree
    from doc to let all Navigation elements build the menu for each page.
    """
    for pages in doc.pages.values():
        for page in pages:  
            navigation = page.select('Navigation')
            if navigation is not None:
                navigation.pageTree = doc.getPageTree() # Get a fresh one for each page

def makeTwitter(styles=styles):
    context = getContext('DrawBot')
    tweets = TwitterPost(styles=styles)
    doc = tweets.newDocument(name='Tweets', viewId=viewId, autoPages=1, context=context)

    return doc

def makeInstagram(styles=styles):
    context = getContext('DrawBot')
    instagram = InstagramPost(styles=styles)
    w, h = InstagramSquare
    doc = instagram.newDocument(name='Instagram', w=w, h=h, context=context)

    # By default, the typesetter produces a single Galley with content and code blocks.    
    t = Typesetter(context, maxImageWidth=MAX_IMAGE_WIDTH)
    mdPath = MD_PATHS[0] # Only make instagram posts from the home page.
    t.typesetFile(mdPath)

    # Header styles
    pad = px(50)
    tPad = px(25)
    h2Style = dict(font='Upgrade-Medium', fontSize=px(120), leading=em(1), textFill=color(1))
    h3Style = dict(font='Upgrade-Regular', fontSize=px(90), leading=em(1), textFill=color(1))
    h4Style = dict(font='Upgrade-Semibold', fontSize=px(90), leading=em(1), textFill=color(1))

    # Filter all h2/h3/image combinations, to make instagram banners.
    bannerData = []
    bs2 = bs3 = bs4 = None
    for e in t.galley.elements:
        if e.isText:
            for run in e.bs.runs:
                if bs2 is None and run.style.get('name') == 'h2':
                    bs2 = context.newString(run.s.strip(), h2Style)
                    bs3 = bs4 = None
                elif bs3 is None and run.style.get('name') == 'h3':
                    bs3 = context.newString(run.s.strip(), h3Style)
                    bs4 = context.newString('', h4Style)
                elif run.style.get('name') == 'h4':
                    bs4 += context.newString(run.s.strip(), h4Style)
                elif run.style.get('name') == 'sup':
                    bs4 += context.newString(run.s.strip(), h4Style)
        elif e.isImage:
            if not None in (bs2, bs3, bs4):            
                bannerData.append((bs2, bs3, bs4, e.path, e.alt))
                bs2 = bs3 = bs4 = None
    

    # Now we have all content, we can create the pages, one per post
    page = doc[1]
    for bs2, bs3, bs4, imagePath, alt in bannerData:
        #print(bs2, bs3, bs4, imagePath)
        iw, ih = context.imageSize(imagePath)
        if iw > ih:
            iw, ih = None, h
        else:
            iw, ih = w, None
        if 'x=center' in alt:
            xAlign = CENTER
            x = w/2
        else:
            xAlign = None
            x = 0
        newImage(path=imagePath, parent=page, x=x, y=0, w=iw, h=ih, xAlign=xAlign)

        if bs2 is not None:
            tw, th = context.textSize(bs2, w=w-2*pad-2*tPad)
            newRect(x=pad, y=h-th-2*tPad, fill=color(rgb='red', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
            newText(bs2, x=pad+tPad, y=h-2*tPad, w=w-2*pad-2*tPad, parent=page)

        if bs3 is not None:
            tw, th = context.textSize(bs3, w=w-2*pad-2*tPad)
            newRect(x=pad, y=h/2-3.5*tPad, fill=color(rgb='darkblue', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
            newText(bs3, x=pad+tPad, y=h/2, w=w-2*pad-2*tPad, parent=page)

        if bs4 is not None:
            tw, th = context.textSize(bs4, w=w-2*pad-2*tPad)
            newRect(x=pad, y=0, fill=color(rgb='blue', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
            newText(bs4, x=pad+tPad, y=2*tPad, w=w-2*pad-2*tPad, parent=page)

        page = page.next
    return doc

def makeTemplate(doc):

    # D E F A U L T

    default = Template('Default', parent=doc)
    wrapper = Wrapper(parent=default) # Create main page wrapper
    
    header = Header(parent=wrapper) # Header to hold logo and navigation elements

    #logoString = doc.context.newString(SITE_NAME)
    Logo(parent=header, logo=SITE_NAME)
    BurgerButton(parent=header)

    # Responsive conditional menus
    Navigation(parent=header)
    MobileMenu(parent=header)

    # Just make a simple content container in this template.
    # Rest of content is created upon request in MarkDown
    Content(parent=wrapper) 

    # Default Footer at bottom of every page.
    Footer(parent=wrapper)

    doc.addTemplate('default', default)
    return default

def makeSite(styles, viewId, context):
    site = Site(styles=styles)
    doc = site.newDocument(name='DDS_Site', viewId=viewId, autoPages=1, context=context)
    
    doc.theme = theme

    view = doc.view
    view.googleAdsAccount = '579-058-0554' 
    view.googleAnalyticsId = 'UA-138308355-1' #'UA-7015465-2' 
    view.resourcePaths = ('css','fonts','scaled', 'code', 'js') # ./images/* get copy/scaled
    view.jsUrls = (
        URL_JQUERY, 
        'js/jquery.bbslider.min.js',
        #URL_MEDIA, 
        #'js/sitemain.js', 
    )
    
    # Generate css by mapping theme.mood on cssPy 
    cssPath = 'css/nanostyle_py.css'
    view.context.b.writeCss(cssPath, cssPy % theme.mood)

    view.cssUrls = (
        'css/jquery.bbslider.css',
        'fonts/webfonts.css', 
        'css/normalized.css', 
        cssPath,
    )
    BASE_FONT_SIZE = 16
    view.jsCode = """
    function setBaseFontSize(){
        /*document.getElementsByTagName('body')[0].style['font-size'] = %d * window.devicePixelRatio + 'px';*/
    }
    window.onload = setBaseFontSize;
    """ % BASE_FONT_SIZE

    # Make the all pages and elements of the site as empty containers, that then can
    # be selected and filled by the composer, using the galley content.
    # Of the MarkDown text can decide to create new elements inside selected elements.
    template = makeTemplate(doc)    

    page = doc[1]
    page.applyTemplate(template) # Copy element tree to page.

    # By default, the typesetter produces a single Galley with content and code blocks.    
    t = Typesetter(view.context, maxImageWidth=MAX_IMAGE_WIDTH)
    for mdPath in MD_PATHS:
        print('Typeset file', mdPath)
        t.typesetFile(mdPath)
    #t.galley.fill = color(1)

    # Create a Composer for this document, then create pages and fill content. 
    composer = Composer(doc)

    # The composer executes the embedded Python code blocks that indicate where content should go.
    # by the HtmlContext. Feedback by the code blocks is added to verbose and errors list
    print('Composing pages')
    targets = dict(doc=doc, page=page, template=template, theme=theme)
    composer.compose(t.galley, targets=targets)

    if VERBOSE:
        if targets['verbose']:
            print('Verbose\n', '\n'.join(targets['verbose']))
        # In case there are any errors, show them.
        if targets['errors']:
            print('Errors\n', '\n'.join(targets['errors']))
    
    # Find the navigation elements and fill them, now we know all the pages.
    print('Make navigation')
    makeNavigation(doc)

    # https://www.hyphenator.net/en/word/...
    #unknownWords = doc.spellCheck(LANGUAGE_EN)
    #if unknownWords:
    #    print(unknownWords)

    return doc

if DO_PDF in EXPORT_TYPES: # PDF representation of the site
    doc = makeSite(styles=styles, viewId='Page', context=context)
    doc.solve() # Solve all layout and float conditions for pages and elements.
    doc.export(EXPORT_PATH + '.pdf')

if DO_FILE in EXPORT_TYPES:
    doc = makeSite(styles=styles, viewId='Site', context=context)
    doc.export(EXPORT_PATH)
    openingPage = 'program-2020.html'
    os.system(u'/usr/bin/open "%s/%s"' % (EXPORT_PATH, openingPage))

if DO_MAMP in EXPORT_TYPES:
    # Internal CSS file may be switched off for development.
    doc = makeSite(styles=styles, viewId='Mamp', context=context)
    mampView = doc.view
    MAMP_PATH = '/Applications/MAMP/htdocs/' 
    filePath = MAMP_PATH + SITE_NAME 
    if VERBOSE:
        print('Site path: %s' % MAMP_PATH)
    if os.path.exists(filePath):
        shutil.rmtree(filePath) # Comment this line, if more safety is required. In that case manually delete.
    doc.export(filePath)

    if not os.path.exists(filePath):
        print('The local MAMP server application does not exist. Download and install from %s.' % view.MAMP_SHOP_URL)
        os.system(u'/usr/bin/open %s' % view.MAMP_SHOP_URL)
    else:
        #t.doc.export('_export/%s.pdf' % NAME, multiPages=True)
        os.system(u'/usr/bin/open "%s"' % mampView.getUrl(SITE_NAME))

if DO_GIT in EXPORT_TYPES: # Not supported for SimpleSite, only one per repository?
    # Make sure outside always has the right generated CSS
    doc = makeSite(styles=styles, viewId='Git', context=context)
    gitView = doc.view
    GIT_PATH = 'docs/' 
    if VERBOSE:
        print('Site path: %s' % MAMP_PATH)
    #if os.path.exists(filePath):
    #    shutil.rmtree(filePath) # Comment this line, if more safety is required. In that case manually delete.
    doc.export(GIT_PATH)

    # Open the css file in the default editor of your local system.
    if 0:
        os.system('/usr/bin/git pull')  
        os.system('/usr/bin/git add *')
        os.system('/usr/bin/git commit -m "Updating website changes."')
        os.system('/usr/bin/git pull')
        os.system('/usr/bin/git push')
        #os.system(u'/usr/bin/open "%s"' % gitView.getUrl(DOMAIN))

if DO_TWITTER in EXPORT_TYPES: 
    doc = makeTwitter(styles=styles)
    doc.export(INSTAGRAM_PATH, multiPages=True)

if DO_INSTAGRAM in EXPORT_TYPES:
    doc = makeInstagram(styles=styles)
    doc.export(INSTAGRAM_PATH)

#else: # No output view defined
#    print('Set EXPORTTYPE to DO_FILE or DO_MAMP or DO_GIT')

print('Done')

