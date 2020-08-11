#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E01_Instagram.py
#
#     Take the content from a MarkDown file, typically one that contains website content.
#     Find the titles of events in a (h2, h3, h4, image) pattern
#     Generate Instagram images for each event.
#
from pagebot import getContext
from pagebot.filepaths import getResourcesPath
from pagebot.publications.instagram import InstagramPost
from pagebot.toolbox.units import px, em, pt
from pagebot.toolbox.color import color, noColor
from pagebot.constants import InstagramSquare, CinemaWide, MAX_IMAGE_WIDTH, CENTER
from pagebot.typesetter import Typesetter
from pagebot.elements import *

context = getContext()

"""
from pagebot.document import Document
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.elements import *
import flat
"""

FEW_SPACES = True

# Example image that has nice areas to put text as example.
imagePath = getResourcesPath() + '/images/pagebot.png'
EXPORT_PATH_PDF = '_export/01_Instagram.pdf'
EXPORT_PATH_PNG = '_export/01_Instagram.png' 
EXPORT_PATH_JPG = '_export/01_Instagram.jpg' 
# Add extra layer
EXPORT_PATH_FEWSPACES_JPG = '_export/01_Instagram_FewSpaces.jpg' 
MD_PATHS = ['DDS-home.md']

h2Style = dict(font='Upgrade-Medium', fontSize=pt(80), leading=em(1), tracking=0.02, textFill=color(1))
h3Style = dict(font='Upgrade-Regular', fontSize=pt(60), leading=em(1), tracking=0.02, textFill=color(0))
h4Style = dict(font='Upgrade-Medium', fontSize=pt(60), leading=em(1), tracking=0.02, textFill=color(1))
supStyle = dict(font='Upgrade-Medium', fontSize=pt(60), leading=em(1), tracking=0.02, textFill=color(1,0,0))
fewSpacesStyle = dict(font='Upgrade-Bold', fontSize=pt(130), leading=em(1), tracking=0.02, textFill=color(1,1,1))

styles = dict(
    h2=h2Style,
    h3=h3Style,
    h4=h4Style,
    sub=supStyle,
)
instagram = InstagramPost(styles=styles)
w, h = pt(InstagramSquare)
doc = instagram.newDocument(name='Instagram', w=w, h=h, context=context)

# By default, the typesetter produces a single Galley with content and code blocks.    
t = Typesetter(context, maxImageWidth=MAX_IMAGE_WIDTH)
mdPath = MD_PATHS[0] # Only make instagram posts from the home page.
t.typesetFile(mdPath)

# Header styles
pad = px(30)
tPadW = px(40)
tPadH = px(20)
lPad = px(8) # Padding of the logo in the square

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
                bs4 += context.newString(run.s.strip(), h4Style) + ' '
            elif run.style.get('name') == 'sup':
                bs4 += ', '#context.newString(run.s.strip(), supStyle) + ' '
    elif e.isImage:
        if not bs3:
            bs3 = context.newString('Program of 2020-2021', h3Style)
        if not bs4:
            bs4 = context.newString('https://designdesign.space', h4Style)
        if not None in (bs2, bs3, bs4):            
            bannerData.append((bs2, bs3, bs4, e.path, e.alt))
            bs2 = bs3 = bs4 = None


# Now we have all content, we can create the pages, one per post
page = doc[1]
# For now direct output, as long as vertical position of text is not accurate
for bs2, bs3, bs4, imagePath, alt in bannerData:
    context.newPage(page.w, page.h)
    bs4.s = bs4.s.split('•')[0].replace('Start', 'Workshop start:').replace(' th ', ', ').replace(' st ', ', ')
    print(bs2.s)
    print(bs3.s)
    print(bs4.s)
    print('---')
    iiw, iih = context.imageSize(imagePath)
    if iiw > iih:
        sc = h/iih
    else:
        sc = w/iiw
    ih = iih * sc
    iw = iiw * sc
    x = y = 0
    if 1 or 'x=center' in alt:
        xAlign = CENTER
        x = w/2 - iw/2
    else:
        xAlign = None
        x = 0
    context.scale(sc)
    context.image(imagePath, (x, y))
    context.scale(1/sc)

    y = h
    if bs2 is not None:
        tw, th = context.textSize(bs2, w=w-2*pad-2*tPadW)
        context.fill(color(0, a=0.82))
        context.b.save()
        context.b.shadow((10, -10), 20, (0, 0, 0, 0.7))
        context.rect(x=pad, y=y-th-2*tPadH-pad, w=w-2*pad, h=th+2*tPadH)
        context.b.restore()
        context.textBox(bs2, (pad+tPadW, y-th-tPadH-pad+bs4.descender/3, w-2*pad-2*tPadW, th))

    y -= th+2*tPadH+pad 
    if bs3 is not None:
        tw, th = context.textSize(bs3, w=w-4*pad-2*tPadW)
        context.b.save()
        context.b.shadow((10, -10), 20, (0, 0, 0, 0.7))
        context.fill(color(1, a=0.82))
        context.rect(x=pad*2, y=y-th-2*tPadH, w=w-4*pad, h=th+2*tPadH)
        context.b.restore()
        context.textBox(bs3, (pad*2+tPadW, y-th-tPadH+bs3.descender/3, w-4*pad-2*tPadW, th))

    tw, th = context.textSize(bs4, w=w-2*pad-2*tPadW)
    context.b.save()
    context.b.shadow((10, -10), 20, (0, 0, 0, 0.7))
    context.fill(color(rgb=0xF44B09, a=0.82))
    context.rect(x=pad, y=0, w=w-2*pad, h=th+2*tPadH)
    context.b.restore()
    context.textBox(bs4, (pad+tPadW, tPadH-3, w-2*pad-2*tPadW, th))

    logoPath = 'images/DesignDesign.Space.png'
    iiw, iih = context.imageSize(logoPath)
    sc = 0.4
    context.b.save()
    context.b.shadow((10, -10), 20, (0, 0, 0, 0.7))
    context.fill(color(0, a=0.82))
    context.rect(w-pad-iiw*sc-2*lPad, th+2*tPadH, iiw*sc+2*lPad, iih*sc+2*lPad)
    context.b.restore()
    context.scale(sc)
    context.image(logoPath, ((w-pad-lPad)/sc - iiw, (th+2*tPadH+lPad)/sc))
    context.scale(1/sc)

    if FEW_SPACES: 
        bs5 = context.newString('Few spaces left', fewSpacesStyle)
        tw, th = context.textSize(bs5, w=w-2*pad-4*tPadW)
        context.b.save()
        context.b.rotate(20)
        context.b.save()
        context.b.shadow((10, -10), 20, (0, 0, 0, 0.7))
        context.fill(color(rgb=0xF44B09, a=0.82))
        context.rect(x=pad*8, y=page.h/2-4*pad-th-2*tPadH, w=w-4*pad, h=th+2*tPadH)
        context.b.restore()
        context.textBox(bs5, (pad*8+tPadW, page.h/2-4*pad-th-tPadH+bs3.descender/3, w-4*pad-2*tPadW, th))
        context.b.restore()
  

    page = page.next

if FEW_SPACES:
    context.saveImage(EXPORT_PATH_FEWSPACES_JPG, multiPage=True)
else:
    context.saveImage(EXPORT_PATH_PDF, multiPage=True)
    context.saveImage(EXPORT_PATH_PNG, multiPage=True)
    context.saveImage(EXPORT_PATH_JPG, multiPage=True)


