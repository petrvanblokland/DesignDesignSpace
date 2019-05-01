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
#     Cards.py
#
from pagebot.contexts.drawbotcontext import DrawBotContext
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import em, p, pt
from pagebot.constants import *
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter

context = DrawBotContext()

H = pt(284) # Rounded mm(100)
W = 2*H
G = pt(16) # Gutter
PAD = pt(32)  # Page padding on all sides
PADDING = (PAD, PAD, PAD+G, PAD)
BACK = pt(14) # mm(5)
BLEED = pt(10)

CW = (W - PAD - G - PAD - G - PAD)/4
GRIDX = [(CW, G), (CW, PAD), (CW, G), (CW, 0)]
FOLDS = [(W/2, None)]

W_COVER = W + BACK
GRIDX_COVER = [(CW, G), (CW, PAD+BACK), (CW, G), (CW, 0)]
FOLDS_COVER = [(W/2, None), (W/2+BACK, None)]

NUM_PAGES = 2*6 # Spreads

MD_PATH = 'Cards.md'

# Get the font object, from te Roboto file that is included in PageBot resources for testing.
f = findFont('Upgrade-Regular')

# Create a new document with 1 page. Set overall size and padding.
# TODO: View grid drawing, etc. does not work properly for originTop=True
doc = Document(w=W, h=H, padding=PADDING, context=context, 
    autoPages=NUM_PAGES, originTop=False, gridX=GRIDX)

view = doc.view
if 0:
    view.showPadding = True
    view.showGrid = True
    view.padding = pt(32)
    view.showRegistrationMarks = True
    view.showCropMarks = True
    view.showFrame = True
else:
    view.padding = 0

for pn in range(1, NUM_PAGES+1):
    page = doc[pn]
    page.padding = PADDING
    page.bleed = BLEED
    c = (0.8, 0.8, 0.8, 0.5)
    if pn in (1, 2):
        page.w = W_COVER
        page.folds = FOLDS_COVER
        page.gridX = GRIDX_COVER
        newRect(parent=page, fill=c, w=BACK, 
            conditions=[Fit2HeightBleeds(), Center2Center()])
    else:
        page.folds = FOLDS        

    page.solve()

# Fill by 
page = doc[1]

# By default, the typesetter produces a single Galley with content and code blocks.    
t = Typesetter(doc.context)
t.typesetFile(MD_PATH)

# Create a Composer for this document, then create pages and fill content. 
composer = Composer(doc)

# The composer executes the embedded Python code blocks that indicate where content should go.
# by the HtmlContext. Feedback by the code blocks is added to verbose and errors list
targets = dict(doc=doc, page=page)
composer.compose(t.galley, targets=targets)

doc.solve()

doc.export('_export/Cards.pdf')