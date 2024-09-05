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
#     CodeForDesigners-TypographicsBanner.py
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
from pagebot.elements import Element, newRect, newTextBox, newImage, newGroup, newLine

P = 16
M = P

TITLE1 = 'Scripting for (graphic) designers'
TITLE2 = 'Discover rules behind your work\nduring this free workshop day.'
TITLE3 = '\nLight coding. Simple examples. Small tools.\nFor starters and experienced coders.\n'


# Export in folder that does not commit to Git. Force to export PDF.
PATH = '../docs/images/'

IMAGES1 = (
    ('pagebotcode.png', [fit2widthsides()]),
)FRAMES = 14

BANNER_DATA = [
    dict(filePath='CodeForDesignersBanner-Typographics2160x1080.gif', 
        w=2160, h=1080, title1=TITLE1, title2=TITLE2, title3=TITLE3, imagePaths=IMAGES1, labelSize=48, titleSize=100, sideImage='BuroKaartViolet.png', l1=4, l2=8, type='Large', padding=50),
    dict(filePath='CodeForDesignersBanner-Typographics1200x400.gif', 
        w=1200, h=400, title1=TITLE1, title2=TITLE2, title3=None, imagePaths=IMAGES1, labelSize=48, titleSize=100, sideImage='BuroKaartYellow.png',
        l1=2, l2=3, type='Small', padding=28),
]


family = getFamily('Upgrade')
fontBook = family.findFont('Book')
fontRegular = family.findFont('Regular')
fontMedium = family.findFont('Medium')
fontBold = family.findFont('Bold')
fontItalic = family.findFont('Italic')

def makeBanner(bd):
    w, h = bd['w'], bd['h']
    imagePaths = bd['imagePaths']
    labelSize = bd['labelSize']
    title1 = bd['title1']
    title2 = bd['title2']
    title3 = bd['title3']
    sideImage = bd['sideImage']
    titleSize = bd['titleSize']
    L1 = bd['l1']
    L2 = bd['l2']
    padding = bd['padding']
    type = bd['type']
    
    context = getContext()
    context.newDrawing()
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template
    doc = Document(w=w, h=h, title=title1, autoPages=FRAMES, context=context,
        originTop=False) # One page, just the cover.

    for pn in range(1, FRAMES+1):
        page = doc[pn] # Get the first/single page of the document.

        page.frameDuration = 0.75
    
        imagePath, imageConditions = imagePaths[0]
        # Background image of the slide
        im = newImage(PATH+imagePath, y=h/FRAMES*(pn-1), conditions=imageConditions, parent=page)
        newImage(PATH+imagePath, y=h/FRAMES*(pn-1)-2*im.h, conditions=imageConditions, parent=page)
        newImage(PATH+imagePath, y=h/FRAMES*(pn-1)-im.h, conditions=imageConditions, parent=page)
        newImage(PATH+imagePath, y=h/FRAMES*(pn-1)+im.h, conditions=imageConditions, parent=page)
        newImage(PATH+imagePath, y=h/FRAMES*(pn-1)+2*im.h, conditions=imageConditions, parent=page)

        ww75 = w*0.75
        ww25 = w*0.25
        bs = context.newString('Type@Cooper\nTypographics', 
            style=dict(font=fontRegular.path, fontSize=w/30, xTextAlign=CENTER, textFill=1, rLeading=1.05, rTracking=0.02))
        tw, th = bs.textSize()
        newRect(fill=(0.15,0.17,0.15,0.7), w=ww75, conditions=(Fit2HeightSides(), Right2RightSide()), parent=page)        
        newTextBox(bs, parent=page, h=th+P, w=ww25, padding=(P/2,P,0,P), fill=(1,0,0), conditions=(Left2LeftSide(), Top2TopSide()))

        # Show design measures
        m = padding*2
        m2 = m/2
        m4 = m/4
        designProcess = newGroup(x=0, y=0, fill=(0.3, 0.32, 0.3, 0.7), w=ww25, h=h-th-P, padding=padding, parent=page)
        design = newImage(PATH+sideImage, y=padding, h=h-th-P-2*padding, fill=None, conditions=[Center2Center()], parent=designProcess) 
        designProcess.solve()
        
        if pn > 1: # Horizontal frame
            newLine(x=design.x-m4, y=design.y, w=design.w+m2, h=0, fill=None, stroke=1, strokeWidth=L1, parent=designProcess)
            newLine(x=design.x-m4, y=design.y+design.h, w=design.w+m2, h=0, fill=None, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 2: # Vertical frame
            newLine(x=design.x, y=design.y-m4, w=0, h=design.h+m2, fill=None, stroke=1, strokeWidth=L1, parent=designProcess)
            newLine(x=design.x+design.w, y=design.y-m4, w=0, h=design.h+m2, fill=None, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn == 4: # Diagonal
            newLine(x=design.x, y=design.y, w=design.w, h=design.h, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
            newLine(x=design.x+design.w, y=design.y, w=-design.w, h=design.h, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
        if pn > 5: # V-lines
            newLine(x=design.x+design.w/2, y=design.y-m4, w=0, h=design.h+m2, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 6: # V-lines
            newLine(x=design.x+design.w*0.35, y=design.y-m4, w=0, h=design.h+m2, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 7: # V-lines
            newLine(x=design.x+design.w*0.92, y=design.y-m4, w=0, h=design.h+m2, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn == 9: # H-lines 1/2
            newLine(x=design.x-m2, y=design.y+design.h*0.5, w=design.w+2*m2, h=0, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 9: # H=lines
            newLine(x=design.x-m2, y=design.y+design.h*0.53, w=design.w+2*m2, h=0, stroke=1, strokeWidth=L1, parent=designProcess)
            newLine(x=design.x-m2, y=design.y+design.h*0.59, w=design.w+2*m2, h=0, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 10: # H=lines
            newLine(x=design.x-m2, y=design.y+design.h*0.24, w=design.w+2*m2, h=0, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 11: # H=lines
            newLine(x=design.x-m2, y=design.y+design.h*0.655, w=design.w+2*m2, h=0, stroke=1, strokeWidth=L1, parent=designProcess)
        if pn > 12: # Diagonal
            newLine(x=design.x, y=design.y, w=design.w, h=design.h*0.53, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
            newLine(x=design.x+design.w, y=design.y, w=-design.w, h=design.h*0.53, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
        if pn > 13: # Diagonal
            newLine(x=design.x, y=design.y+design.h*0.59, w=design.w, h=design.h-design.h*0.59, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
            newLine(x=design.x+design.w, y=design.y++design.h*0.59, w=-design.w, h=design.h-design.h*0.59, fill=None, stroke=(1, 0, 0), strokeWidth=L2, parent=designProcess)
         
        C0 = 1     
        C1 = C2 = (0, 1, 0.1, 0.95)
        if pn > 10:
            C2 = C0
        
        if type == 'Small':    
            bs = context.newString(title1+'\n', style=dict(font=fontMedium.path, textFill=C0, fontSize=w/20, rTracking=0.015, rLeading=1.25))
            bs += context.newString(title2+'\n', style=dict(font=fontBook.path, textFill=C1, fontSize=w/20, rLeading=1.2, rTracking=0.03))
            if title3 is not None:
                bs += context.newString(title3+'\n', style=dict(font=fontRegular.path, textFill=1, fontSize=w/30, rLeading=1.2, rTracking=0.03))
            bs += context.newString('By DrawBot + PageBot + Petr van Blokland, June 17th', style=dict(font=fontRegular.path, textFill=C2, fontSize=w/33, rTracking=0.030, rLeading=1.8))
            newTextBox(bs, parent=page, x=ww25, y=0, padding=(w/30,0,0,w/30), w=ww75+w/100, conditions=[Fit2HeightSides()])
        else:
            bs = context.newString(title1+'\n', style=dict(font=fontMedium.path, textFill=C0, fontSize=w/20, rTracking=0.015, rLeading=1.25))
            bs += context.newString(title2+'\n', style=dict(font=fontBook.path, textFill=C1, fontSize=w/20, rLeading=1.2, rTracking=0.03))
            if title3 is not None:
                bs += context.newString(title3+'\n', style=dict(font=fontRegular.path, textFill=1, fontSize=w/27, rLeading=1.2, rTracking=0.03))
            bs += context.newString('By DrawBot + PageBot + Petr van Blokland, June 17th', style=dict(font=fontRegular.path, textFill=C2, fontSize=w/33, rTracking=0.030, rLeading=1.8))
            newTextBox(bs, parent=page, x=ww25, y=0, padding=(w/30,0,0,w/30), w=ww75+w/100, conditions=[Fit2HeightSides()])
            
        score = page.evaluate()
        if score.fails:
            page.solve()

    # Evaluate again, result should now be >= 0
    return doc

for bannerData in BANNER_DATA:
    d = makeBanner(bannerData)
    d.export('_export/'+bannerData['filePath'])

