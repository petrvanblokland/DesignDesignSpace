~~~
doc.title = 'Design&nbsp;Design&nbsp;Space'

doc.footerHtml = """Let us know what you think. Do you have any questions for us? <a href="mailto:info@designdesign.space?subject=Tell me more about DesignDesign.Space">info@designdesign.space</a>"""

# Uncomment to see cssId/cssClass markers in the page
#doc.view.showIdClass = True

# Page (Home)
#	Wrapper
#		Header 
#			Logo (+BurgerButton)
#			Navigation/TopMenu/MenuItem(s)
#      Content
#  			Banner
#  			SlideShow (on Home)
#      		Slides
#      		SlideSide
#			Section(s)
#				Introduction
#				Main
#				Mains
#					Main
#				Side
#				Sides
#					Side
#		Footer
#
# ----------------------------------------
# index.html
# ----------------------------------------
page.name = 'Home'
page.url = 'index.html'
content = page.select('Content')
box = content.newBanner()

# Which studies can we offer you in 2020?
~~~
# Free workshops in 2020
~~~
from pagebot.constants import *
slideshow = content.newSlideShow(h=300, slideW='100%', slideH=300, startIndex=3, autoHeight=True, carousel=2, dynamicHeight=False, transition='slide', easing=CSS_EASE, frameDuration=4, duration=0.7, pauseOnHit=True, randomPlay=False)
box = slideshow.slides
~~~

![Color squares cover y=top x=center](images/PepperTomColorSquares.png)
![White painted grid cover y=top x=center](images/IMG_1107.jpg)
![Sketched letters cover y=center](images/IMG_2848.jpg)
![Blue Orange cloth cover y=top x=center](images/IMG_3145.jpg)
![G-Cube variables cover y=center x=center](images/GN-Cube-Variable-e.png)
![Sketched toys cover y=top x=center](images/IMG_4905.jpg)
![DrawBotHomePage cover y=top x=center](images/DrawBotHomePage.png)
![Collage Blue and pear cover y=top x=center](images/IMG_8677.jpg)
![Theme colors cover y=top x=center](images/ThemeColorsByDocument_5.png)
![Sketching details cover y=top x=center](images/DesignModels2.038.png)
![Shells on green wood cover y=top x=center](images/IMG_0752.jpg)
![Model interior cover y=center x=left](images/IMG_E8927.jpg)
![Affiche Rituelen cover y=bottom x=center](images/affiche_rituelen.png)
![Triangle pattern cover y=bottom x=center](images/IMG_1447.jpg)
![Corner write-black-green cover y=top x=center](images/IMG_6994.jpg)
![Den Bosch letter door cover y=top x=center](images/IMG_6129.jpg)
![Interior sketch cover y=top x=center](images/IMG_E8874.jpg)

~~~ 
box = slideshow.side
~~~

### Develop your process. Expand your skills.

## Temporary free workshops

In Corona world, life has changed. Working and studying from home is the new reality for many. To distract yourself a bit from this new parallel universe, the question is: **What to do?** DesignDesign.Space offers you a series of **free workshops** in the upcoming months. Check them out.

#[How this works](#how-free-workshops-work)
#[Why we offer this for free](#why-we-offer-this-for-free)
<br/>
# [Contact us](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop)

~~~
box = content.newIntroduction()
~~~

# Working from home? Studying online in Corona world? DesignDesign.Space offers a series of **free workshops**. Check the dates and topics. Subscribe by [e-mail](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop). Limited places. First come, first served.

~~~ 
#box = section.newCropped()
## ![Sponsoring Typographics2019]()
#![Typographics2019Logo.png x=center y=center](images/Typographics2019Logo.png)
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
### Wednesday hangouts 19:00–22:00 Central European Time

* *Each workshop spans 2 weeks of work, including 3 hangouts, Slack and document sharing.*
* *Other times in the day are possible, depending on other participants and where you live.*
* *Some experience with typography and graphic design is helpful in the workshops.*

~~~
box = section.newCropped()
~~~
![cover y=top](images/IMG_8940.jpg)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Coding your designs in [DrawBot](http://www.drawbot.com) [Fully booked, currently running]

### March 25<span class="sup">th</span> + April 1<span class="sup">st</span> + 8<span class="sup">th</span>

* Start with one of your designs, or select a favourite publication.
* Analyze the existing layout and prepare measurements to be coded.
* Learn to write a program that generates a similar PDF document.
* Design methods to generalize your code for other publications.
* Use the coding in your daily sketching process.

The workshop assumes no experience with programming in Python. An Apple computer is required to run the DrawBot application. 

*DrawBot is an Open Source application by Just van Rossum and Frederik Berlaen*

~~~
box = section.newCropped()
~~~
![cover y=top x=center](images/DrawBotHomePage.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
## What does your design space look like? 

### April 15<span class="sup">th</span> + 22<span class="sup">th</span> + 29<span class="sup">th</span> [7 places left]

* Take your current workspace as a start to analyse.
* Learn to look at the space from different points of view.
* What do you want to keep? And what could be improved?
* Develop sketching techniques to design your environment.

The workshop requires no prior experience with 3D design.

*If you applied, and did not get feedback from us yet, please email again.*

~~~
box = section.newCropped()
~~~
![Model interior cover y=center](images/IMG_E8927.jpg)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Type design crits [Fully booked]

### May 6<span class="sup">th</span> + 13<span class="sup">th</span> + 20<span class="sup">th</span> 

* Start with one of your type designs that is being developed. Or take one of your favourite existing typefaces.
* We ask questions, you do the work, getting valuable feedback and directions.
* Develop some proofing tools, using Python and DrawBot.
* Addressing topics, such as process, methods, variable design spaces, features and tools.

The workshop assumes no experience with programming in Python. An Apple computer is required to run the DrawBot application. 

*If you applied, and did not get feedback from us yet, please email again.*

~~~
box = section.newCropped()
~~~
![cover y=top](images/IMG_5640.jpg)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Coding typography in Python and CSS [Fully booked]

### May 27<span class="sup">th</span> + June 3<span class="sup">rd</span> + 10<span class="sup">th</span> 

* The workshop dives into the most important parameters, that make good typography. 
* Learn about the difference between Python parameters (e.g. generating PDF documents) and CSS (used in websites).
* We may have a look at [PageBot](https://github.com/PageBot/PageBot/blob/master/README.md)
* Investigate methods to connect this knowledge with your daily design practice.

*If you applied, and did not get feedback from us yet, please email again.*

~~~
box = section.newCropped()
~~~
![cover y=top](images/ATFSpecemin-Code04.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Simple sketching techniques 

### June 17<span class="sup">th</span> + 24<span class="sup">th</span> + July 1<span class="sup">st</span> [7 places left]

* What is your design process like, before you open InDesign or a font editor?
* We will look into exercises by sketching paper, as well as connecting them to your digital tools. 
* Learn to appreciate short design cycles and mixed techniques.

*If you applied, and did not get feedback from us yet, please email again.*

~~~
box = section.newCropped()
~~~
![cover y=top](images/DesignModels2.038.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Running a small studio 

### July 8<span class="sup">th</span> + 15<span class="sup">th</span> + 22<span class="sup">nd</span> [4 places left]

* Tips and tricks on how to deal with customers.
* Methods for planning and pricing. 
* Design your process. Small iterations. Testing and feedback.

*If you applied, and did not get feedback from us yet, please email again.*

~~~
box = section.newCropped()
~~~
![cover y=top](images/BNO-BuroBoek2008.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
<a name="how-free-workshops-work"/>
## How free workshops work: some rules

#### Subscribing

* Subscribe for **just one** workshop of your choice, by sending an e-mail to [info@designdesign.space](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop)
* Describe your daily profession and how that relates to the topic of your selected workshop. Add some samples of your work.
* Workshops are limited to a maximum of 10 students. First come, first served. 
 
#### The workshop

* Using some small assignments, we challenge you to sketch, think, design and give feedback to others.
* Each workshop spans several sessions. There is enough time between them, to give you the opportunity to process the questions of one session into the next one.
* We create an online platform, accessible for all students of the workshop, to share work, questions, comments and documents.
* You are encouraged to join the whole workshop from start to end, following all sessions, not occupying the space for another designer.

#### And after...

* DesignDesign.Space would appreciate to publish some of your work on this website.
* Successfully finishing one of the free workshops gives the right to **20% reduction** on one of the other DesignDesign.Space studies.

---
<a name="why-we-offer-this-for-free"/>
## Why we offer this for free

We like to share and express our solidarity with you.

Also, we are educators and we are designers, too. That means, we are curious how others design their design processes. We are open for suggestions about the workshops and about how you perceive the way we teach. For us, educating other designers is as much of a challenge as any design process.

#### New topics
[Send us your request](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop) for topics that we never thought about. Or ideas about how the workshops can be improved. Lure us into teaching you in a different way than what we suggest here. We’ll likely take the challenge.

#### We love your feedback
If you tell us what you want to study by mail or in a first free online hangout, we are happy to make suggestions. What would you like to achieve? Seeking a sparring partner for an interesting new design project? Improving your latent skills, while training your self-discipline? Or simply needing a refreshing break from your normal design practice? 

---

## Other study suggestions

* [Type design](studies-type_design.html)
* [Typography](studies-typography.html)
* [Graphic design](studies-graphic_design.html)
* [Design spaces](studies-design_spaces.html)
* [Design practice](studies-design_practice.html)
* [Design education](studies-design_education.html)

These studies are regular DesignDesign.Space products. Check [here](pricing.html) for prices.

#### Typeface of this website: [TYPETR Upgrade](http://upgrade.typenetwork.com)

~~~
box = section.newCropped()
~~~

![w=100% y=top](images/BK-Studio-Design.png)
