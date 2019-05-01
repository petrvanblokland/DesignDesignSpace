~~~
#4-1
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import color, whiteColor
from pagebot.fonttoolbox.objects.font import findFont
font = findFont('Upgrade-Book')

newRect(parent=page, fill=(1, 0, 0), conditions=[Fit2Bleed()])
newImage('images/DesignDesign.Space.png', w=page.h, parent=page, conditions=[Right2RightSide(), Bottom2BottomSide()])

style = dict(font=font, fontSize=pt(16), leading=pt(18), textFill=whiteColor, tracking=em(0.01))
t = doc.context.newString('Scales\nModels\nExercises', style=style)
newTextBox(t, parent=page, w=200, h=250, conditions=[Shrink2TextBounds(), Top2Top(), Right2Right()])

~~~

~~~
#2-3
page = page.next
newRect(parent=page, fill=0, conditions=[Fit2Bleed()])
newImage('images/IMG_9289.jpg', w=page.w+page.bleedLeft+page.bleedRight, h=page.h, parent=page, conditions=[Right2RightBleed(), Middle2Middle()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

~~~
#8-5 Type (outside)
page = page.next
newTextBox('Type 8', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Type 5', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

~~~

~~~
#6-7 Type (inside)
page = page.next
newTextBox('Type 6', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Type 7', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

~~~
#12-9 Typography (outside)
page = page.next
newTextBox('Typography 12', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Typography 9', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

~~~

~~~
#10-11 Typography (inside)
page = page.next
newTextBox('Typography 10', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Typography 11', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

~~~
#16-13 Graphic design (outside)
page = page.next
newTextBox('Graphic design 16', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Graphic design 13', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

~~~

~~~
#14-15 Graphic Design (inside)
page = page.next
newTextBox('Graphic design 14', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Graphic design 15', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

~~~
#20-17 Design spaces (outside)
page = page.next
newTextBox('Design spaces 20', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Design spaces 17', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

~~~

~~~
#18-19 Design spaces (inside)
page = page.next
newTextBox('Design spaces 18', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Design spaces 19', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

~~~
#24-21 Design practice (outside)
page = page.next
newTextBox('Design practice 24', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Design practice 21', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

~~~

~~~
#22-23 Design practice (inside)
page = page.next
newTextBox('Design practice 22', parent=page, w=100, h=50, conditions=[Top2Top(), Left2Left()])
newTextBox('Design practice 23', parent=page, w=100, h=50, conditions=[Top2Top(), Right2Right()])

newRect(parent=page, h=pt(32+10), fill=color(name='orange'), conditions=[Left2LeftBleed(), Fit2RightBleed(), Bottom2BottomBleed()])
~~~

