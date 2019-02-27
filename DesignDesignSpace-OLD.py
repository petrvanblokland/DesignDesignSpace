# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Free to use. Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     DesignDesignSpace.py
#
#     Build automatic website for designdesign.space, hosted in github.
#
#     http://designdesign.space
#     http://localhost:8888/designdesignspace/index.html
#
#
# 
import os

from pagebot.contexts.htmlcontext import HtmlContext

from pagebot.typesetter import Typesetter
from pagebot.composer import Composer
from pagebot.publications.publication import Publication 
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.publications.website import Website
from pagebot.contexts.drawbotcontext import DrawBotContext
from pagebot.toolbox.units import p, pt, em
from pagebot.toolbox.color import blackColor, color

NAME = 'DesignDesignSpace'

# Path to markdown file, including Python code blocks.
#MD_PATH = u"Site.md"
MD_PATH = u"Program2019-11-15.md"
NAME = 'designdesignspace'
DOMAIN = 'designdesign.space'

DO_GALLEY = False
DO_FILE = True
DO_GIT = False
DO_MAMP = False
FINDER_PATH = 'resources'

if DO_GALLEY:
    context = DrawBotContext()

    leading = em(1.4)
    styles = dict(
        body=dict(font='Georgia', fontSize=pt(10), leading=leading, textFill=blackColor),
        h1=dict(font='Verdana-Bold', fontSize=pt(36), leading=leading, textFill=0.1),
        h2=dict(font='VerdanaBold', fontSize=pt(24), leading=leading, textFill=0.1),
        h3=dict(font='Georgia', fontSize=pt(18), leading=leading, textFill=blackColor),
        h4=dict(font='Georgia', fontSize=pt(12), leading=leading, textFill=blackColor),
        h5=dict(font='Georgia-Bold', fontSize=pt(10), leading=leading, textFill=blackColor),
        p=dict(font='Georgia', fontSize=pt(10), leading=leading, textFill=blackColor),
        li=dict(font='Verdana', fontSize=pt(10), leading=leading, textFill=blackColor),
        em=dict(font='Georgia-Bold'),
    )
else:
    context = HtmlContext()
    styles = None # Use default Typesetter styles. Will be defined by CSS in the site.

class Website(Publication):
    pass

website = Website(FINDER_PATH)

# Create a Typesetter for this context, then create elements to compose on pages. 
# As no Galley instance is supplied to the Typesetter, it will create one.
t = Typesetter(context, styles=styles)

# Parse the markdown content and execute the embedded Python code blocks.
# The code blocks, global defined feedback variables and text content are in the 
# typesetter t.galley.
t.typesetFile(MD_PATH)

galley =  t.galley # Get the parsed elements: TextBox, Image and CodeBlocks.

if DO_GALLEY: # Show the cumulated elements on the galley in A4 PDF, interpreting the MarkDown.
    from pagebot.constants import A4Rounded

    w, h = A4Rounded
    doc = website.newDocument(name=NAME, w=w, h=h, autoPages=1, context=context)
    view = doc.view
    view.showPadding = True
    view.showSourceCode = True

    page = doc[1]
    page.padding = p(5)
    for e in galley.elements:
        e.parent = page
        e.w = page.pw
        e.conditions = (Left2Left(), Float2Top())
        page.solve()
        if e.bottom < page.pb and page.top < page.h - page.pt:
            page = page.next
            e.parent = page
            page.padding = p(5)

    page.solve()
    doc.export('_export/%s.pdf' % doc.name)

elif DO_FILE:
    # Create the site a local static HTML/CSS files.
    from pagebot.composer import Composer
    doc = website.newDocument(name=NAME, autoPages=1, context=context, viewId='Site')
    view = doc.view 
    view.resourcePaths = ('resources/css','resources/fonts','resources/images','resources/js')

    composer = Composer(doc)
    composer.compose(galley)
    doc.export(path=NAME) # Use name as direction to export the website to

elif DO_MAMP:
    # Internal CSS file may be switched of for development.
    #t.doc.info.cssPath = 'resources/sources/pagebot.css'
    view = doc.newView('Mamp')

    if not os.path.exists(view.MAMP_PATH):
        print('The local MAMP server application does not exist. Download and in stall from %s.' % view.MAMP_SHOP_URL)
        os.system(u'open %s' % view.MAMP_SHOP_URL)
    else:
        doc.build(path=NAME)
        #t.doc.export('_export/%s.pdf' % NAME, multiPages=True)
        os.system(u'open "%s"' % view.getUrl(NAME))

elif DO_GIT:
    # Make sure outside always has the right generated CSS
    doc.info.cssPath = 'sources/pagebot.css'
    view = t.doc.newView('Git')
    doc.build(path=NAME)
    # Open the css file in the default editor of your local system.
    os.system('git pull; git add *;git commit -m "Updating website changes.";git pull; git push')
    os.system(u'open "%s"' % view.getUrl(DOMAIN))

else:
    print('Select DO_GALLEY, DO_FILE, DO_MAMP or DO_GIT')

print('Done') 

