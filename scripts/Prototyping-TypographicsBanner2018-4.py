#!/usr/bin/env python
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     Prototyping-TypographicsBanner.py
#
from pagebot.contexts.platform import getContext
# Create random title and names
from pagebot.contributions.filibuster.blurb import blurb

from pagebot.toolbox.transformer import darker
# Get function to find the Roboto family (in this case installed in the PageBot repository
from pagebot.fonttoolbox.objects.family import getFamily
# Creation of the RootStyle (dictionary) with all
# available default style parameters filled.
from pagebot.style import getRootStyle, B4, CENTER, MIDDLE, TOP, RIGHT
# Document is the main instance holding all information
# about the document togethers (pages, styles, etc.)
from pagebot.document import Document
# Import element layout conditions.
from pagebot.conditions import *
from pagebot.elements import newRect, newTextBox, newImage

P = 16
M = P

TITLE1 = 'Rapid prototyping'
TITLE2 = 'for graphic designers'
#TITLE2 = 'Python scripting for graphic designers: public workshop (1 day)'

# Export in folder that does not commit to Git. Force to export PDF.
PATH = '../docs/images/'

IMAGES1 = (
    ('fs.034.jpeg', (fit2widthsides(), Top2TopSide())),
    ('img_1520bwlow.jpg', (fit2widthsides(), Top2TopSide())),
    ('designmodels2.038.png', (fit2widthsides(), Top2TopSide())),
    ('img_4037.jpg', (fit2widthsides(), Top2TopSide())),
    ('pagebotcode.png', (fit2widthsides(), Top2TopSide())),
    ('img_1488.jpg', (fit2widthsides(), Middle2Middle())),
    ('img_1132.jpg', (fit2widthsides(), Top2TopSide())),
)FRAMES = len(IMAGES1)
IMAGES2 = (
    ('img_1487.jpg', (fit2widthsides(), Top2TopSide())),
    ('img_1520.jpg', (fit2widthsides(), Top2TopSide())),
    ('dsgnwk_0665bw.jpg', (fit2widthsides(), Top2TopSide())),
    ('img_1520bwlow.jpg', (fit2widthsides(), Top2TopSide())),
    ('img_1132.jpg', (fit2widthsides(), Top2TopSide())),
    ('pagebotcode.png', (fit2widthsides(), Top2TopSide())),
)

#BANNER_DATA = [
#    dict(filePath='ProtypingDDSBanner-Typographics1200x400.gif', w=1200, h=400, title1=TITLE1, #title2=TITLE2, imagePaths=IMAGES1, labelSize=48, titleSize=200),
#]
BANNER_DATA = [
    dict(filePath='ProtypingDDSBanner-Typographics800x300.gif', cover, h=300, title1=TITLE1, title2=TITLE2, imagePaths=IMAGES1, labelSize=48, titleSize=200),
]

family = getFamily('Upgrade')
fontBook = family.findFont('Book')
fontRegular = family.findFont('Regular')
fontMedium = family.findFont('Medium')
fontBold = family.findFont('Bold')
fontItalic = family.findFont('Italic')

def makeBanner(bd):
    u"""Demo random book cover generator."""
    w, h = bd['w'], bd['h']
    imagePaths = bd['imagePaths']
    labelSize = bd['labelSize']
    title1 = bd['title1']
    title2 = bd['title2']
    titleSize = bd['titleSize']
    
    context = getContext()
    context.newDrawing()
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template
    doc = Document(w=w, h=h, title=title1, autoPages=FRAMES, context=context,
        originTop=False) # One page, just the cover.

    A = (1,1,1,0.5)
    B = (1,0,1,0.8)
    C = (1,1,1,0.8)
    COLORS = (
        (B, B, A),
        (B, A, B),
        (B, B, A),
        (A, B, B),
        (B, B, A),
        (B, A, B),
        (A, B, B),
    )
    for pn in range(1, FRAMES+1):
        page = doc[pn] # Get the first/single page of the document.

        page.frameDuration = 1.5
    
        imagePath, imageConditions = imagePaths[pn-1]
        # Background image of the slide
        newImage(PATH+imagePath, conditions=imageConditions, parent=page)

        ww75 = w*0.75
        newRect(fill=(0.05,0.05,0.4,0.8), w=ww75, conditions=(Fit2HeightSides(), Right2RightSide()), parent=page)
        
        ww25 = w*0.25
        bs = context.newString('Type@Cooper\nTypographics', style=dict(font=fontRegular.path, fontSize=w/30, xTextAlign=CENTER, textFill=1, rLeading=1.05, rTracking=0.02))
        tw, th = bs.textSize()
        newTextBox(bs, parent=page, h=th+P, w=ww25, padding=(P/2,P,0,P), fill=(1,0,0,0.8), conditions=(Left2LeftSide(), Top2TopSide()))

        bs = context.newString(title1+'\n', style=dict(font=fontMedium.path, textFill=C, fontSize=w/11, rTracking=0.015, rLeading=1.25))
        bs += context.newString(title2+'\n', style=dict(font=fontBook.path, textFill=C, fontSize=w/12, rLeading=0.95))
        bs += context.newString('SKETCHING,', style=dict(font=fontRegular.path, textFill=COLORS[pn-1][0], fontSize=w/24, rTracking=0.1, rLeading=1.3))
        bs += context.newString(' CODING', style=dict(font=fontRegular.path, textFill=COLORS[pn-1][1],fontSize=w/24, rTracking=0.1, rLeading=1.3))
        bs += context.newString(' & ', style=dict(font=fontRegular.path, textFill=A, fontSize=w/24, rTracking=0.1, rLeading=1.3))
        bs += context.newString('MAKING\n', style=dict(font=fontRegular.path, textFill=COLORS[pn-1][2], fontSize=w/24, rTracking=0.1, rLeading=1.3))
        bs += context.newString('Petr van Blokland June 11-13', style=dict(font=fontRegular.path, textFill=C, fontSize=w/17.5, rTracking=0.034, rLeading=1.2))
        newTextBox(bs, parent=page, x=ww25, y=0, padding=(0,0,0,w/30), w=ww75+w/100, conditions=[Fit2HeightSides()])

        score = page.evaluate()
        if score.fails:
            page.solve()

    # Evaluate again, result should now be >= 0
    return doc

for bannerData in BANNER_DATA:
    d = makeBanner(bannerData)
    d.export('_export/'+bannerData['filePath'])

