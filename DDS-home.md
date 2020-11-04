~~~
from pagebot.toolbox.color import color
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

# Workshops in 2020-2021

<!--
~~~
section = content.newSection()
box = section.newMain(cssClass='youtubelink')

box = box.newMovie(url='https://player.vimeo.com/video/445611312')

~~~

![](images/TypeTricksTroves-Cover.png)

~~~
box = section.newSide(cssClass='youtubeside')
~~~
# Type: Tricks & Troves

## Watch the new lecture. Any of these subjects can be the topic of your new study.

* 2 weeks online workshop
* Limited to 8 students
* Interactive lessons
* Exercises and feedback
* 4<span class="sup">th</span> workshop free

# <a href="https://docs.google.com/forms/d/1vLKGROUx03Sm3QGWEwuP1f7Uo1v4qQCmG1FlaxOT88A" target="external">Subscribe here</a>

# [Contact us](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop)

-->

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
![Collage Coffee pot and textile y=top x=center](images/IMG_6704.jpg)
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

# Develop your process. Expand your skills.

* 2 weeks online workshop
* Limited to 8 students
* Interactive lessons
* Exercises and feedback
* 4<span class="sup">th</span> workshop free

# <a href="https://docs.google.com/forms/d/1vLKGROUx03Sm3QGWEwuP1f7Uo1v4qQCmG1FlaxOT88A" target="external">Subscribe here</a>

# [Contact us](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop)


~~~
box = content.newIntroduction()
~~~

# Working from home? Studying online in the Corona world? Select the workshops you like. Develop your profession. <a href="https://docs.google.com/forms/d/1vLKGROUx03Sm3QGWEwuP1f7Uo1v4qQCmG1FlaxOT88A" target="external">Subscribe here</a>
~~~ 
#box = section.newCropped()
## ![Sponsoring Typographics2020]()
#![Typographics2020Logo.png x=center y=center](images/Typographics2020Logo.png)
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Workshops: what is it like?

Each online workshop runs for 2 weeks, including live lectures, addressing theory, showing examples and giving feedback on the exercises that you do.

* 2 weeks, from Monday to Sunday;
* Over 12 hours of live interactive hangouts with theory, models, templates and example documents;
* Maximum of 8 participants per workshop;
* Intensive exercises and daily personal feedback;
* The result of the exercises is shared on a closed Slack channel for the duration of the workshop;
* Feedback comes from the educators and the other students;
* DesignDesign.Space offers a safe online study environment, where any question can be asked;
* €290 per workshop;
* Every 4<span class="sup">th</span> workshop is free.

Some workshops combine as a sequence. It is recommended to do them in the right order to get the best continuation.

~~~
box = section.newCropped()
~~~
![cover y=top x=center](images/DSGNWK_0665BW.jpg)


~~~
section = content.newSection()
box = section.newMain()
~~~
<a name="planned-workshops-by-category"/>

## Planned workshops by category

### Programming

<!--
##### <span class="tab">2020-08-24</span> • [Basic coding in Python #1: Design by parameters (PY1)](#PY1)
##### <span class="tab">2020-09-07</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2020-10-19</span> • [Coding simple scripted tools (PY3)](#PY3)
-->
##### <span class="tab">2020-11-02</span> • [== NOW RUNNING == Coding tools with a user interface (PY4)](#PY4)
##### <span class="tab">2020-11-16</span> • [== Few spaces left == Basic coding in Python #1: Design by parameters (PY1)](#PY1)
##### <span class="tab">2020-11-30</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2021-01-04</span> • [Coding simple scripted tools (PY3)](#PY3)
##### <span class="tab">2021-01-18</span> • [Coding tools with a user interface (PY4)](#PY4)
##### <span class="tab">2021-02-15</span> • [Basic coding in Python #1: Design by parameters (PY1)](#PY1)
##### <span class="tab">2021-03-01</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2021-03-15</span> • [Scripting for RoboFont (PY5)](#PY5)
##### <span class="tab">2021-03-29</span> • [Coding simple scripted tools (PY3)](#PY3)
##### <span class="tab">2021-04-12</span> • [Coding tools with a user interface (PY4)](#PY4)

### Process 

<!--
##### <span class="tab">2020-09-21</span> • [Visual grammar #1: The seven parameters of Bertin](#visual-grammar1)
##### <span class="tab">2020-10-05</span> • [Visual grammar #2: Balance diversity & coherency](#visual-grammar2)
-->
##### <span class="tab">2020-11-16</span> • [== Few spaces left == General sketching techniques (SK1)](#SK1)
##### <span class="tab">2020-11-30</span> • [Running a studio #1: Moodboards & presentations (ST1)](#ST1)
##### <span class="tab">2020-12-14</span> • [Running a studio #2: Requirements, quotes & plannings (ST2)](#ST2)
##### <span class="tab">2021-04-26</span> • [Visual grammar #1: The seven parameters of Bertin (VG1)](#VG1)
##### <span class="tab">2021-05-10</span> • [Visual grammar #2: Balance diversity & coherency (VG2)](#VG2)

### Type design

##### <span class="tab">2020-12-14</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2021-01-18</span> • [Basic principles of type design: For graphic designers (TY1)](#TY1)
##### <span class="tab">2021-02-01</span> • [Contrast principles of type design (TY2)](#TY2)
##### <span class="tab">2021-02-15</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2021-03-01</span> • [Sketching, feedback & planning in type design (TY4)](#TY4)
##### <span class="tab">2021-04-26</span> • [Design design spaces for Variable Fonts (TY6)](#TY6)
##### <span class="tab">2021-05-10</span> • [Design the process and tools for Variable Fonts (TY7)](#TY7)
##### <span class="tab">2021-06-07</span> • [Sketching type (TY3)](#TY3)
##### <span class="tab">2021-06-21</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2021-07-05</span> • [Designing a script (TY8](#TY8)
##### <span class="tab">2021-07-19</span> • [Coding your spacing/kerning tool (TY9)](#TY9)

### Graphic design

##### <span class="tab">2021-02-01</span> • [Basics of logo design (LO1)](#LO1)
##### <span class="tab">2021-03-15</span> • [Coding advanced logo variations (LO2)](#LO2)
##### <span class="tab">2021-03-29</span> • [Basics of typography, grids & layout (GD1)](#GD1)
##### <span class="tab">2021-04-12</span> • [Coding advanced typography & layouts for print and web (GD2)](#GD2)
##### <span class="tab">2021-05-24</span> • [Selecting typefaces (GD3)](#GD3)
##### <span class="tab">2021-06-07</span> • [Coding type specimens (GD4)](#GD4)
##### <span class="tab">2021-06-21</span> • [Design and code info-graphics with databases (IG1)](#IG1)

### Design education

##### <span class="tab">2021-01-04</span> • [Teaching Design Education: online, exercises, feedback & evaluation (DE1)](#DE1)
##### <span class="tab">2021-05-24</span> • [Teaching simulations and design games (DE2)](#DE2)

### Design Game

##### <span class="tab">2020-12-29/30</span> • [== Free workshop == Design Game Pentathlon 5 Rounds (DG1)](#DG1)
##### <span class="tab">2021-03-09/10</span> • [== Free workshop == Design Game Pentathlon 5 Rounds (DG1)](#DG1)

### Spacial design

##### <span class="tab">2021-07-05</span> • [Basic exhibition design (SD1)](#SD1)
##### <span class="tab">2021-07-19</span> • [Workspace design (SD2)](#SD2)


~~~
box = section.newCropped()
~~~
![cover y=top](images/BK-Interaction-Design.png)

~~~
section = content.newSection()
box = section.newMain()
~~~

## Planned workshops by date

~~~
box = box.newInfo()
~~~

### 2020

<!--
##### <span class="tab">2020-08-24</span> • [Basic coding in Python #1: Design by parameters (PY1)](#PY1)
##### <span class="tab">2020-09-07</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2020-09-21</span> • [Visual grammar #1: The seven parameters of Bertin](#visual-grammar1)
##### <span class="tab">2020-10-05</span> • [Visual grammar #2: Balance diversity & coherency](#visual-grammar2)
##### <span class="tab">2020-10-19</span> • [Coding simple scripted tools (PY3)](#PY3)
-->
#### November
##### <span class="tab">2020-11-02</span> • [== NOW RUNNING == Coding tools with a user interface (PY4)](#PY4)
##### <span class="tab">2020-11-16</span> • [== Few spaces left == General sketching techniques (SK1)](#SK1)
##### <span class="tab">2020-11-16</span> • [== Few spaces left == Basic coding in Python #1: Design by parameters (PY1)](#PY1)
##### <span class="tab">2020-11-30</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2020-11-30</span> • [Running a small studio #1: Moodboards & presentations (ST1)](#ST1)

#### December
##### <span class="tab">2020-12-14</span> • [Running a small studio #2: Requirements, quotes & plannings (ST2)](#ST2)
##### <span class="tab">2020-12-14</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2020-12-29/30</span> • [==Free workshop== Design Game Pentathlon 5 Rounds (DG1)](#DG1)

### 2020

#### January
##### <span class="tab">2021-01-04</span> • [Teaching Design Education: online, exercises, feedback & evaluation (DE1)](#DE1)
##### <span class="tab">2021-01-04</span> • [Coding simple scripted tools (PY3)](#PY3)
##### <span class="tab">2021-01-18</span> • [Coding tools with a user interface (PY4)](#PY4)
##### <span class="tab">2021-01-18</span> • [Basic principles of type design: For graphic designers (TY1)](#TY1)

#### February
##### <span class="tab">2021-02-01</span> • [Basics of logo design (LO1)](#LO1)
##### <span class="tab">2021-02-01</span> • [Contrast principles of type design (TY2)](#TY2)
##### <span class="tab">2021-02-15</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2021-02-15</span> • [Basic coding in Python #1: Design by parameters (PY1)](#PY1)

#### March
##### <span class="tab">2021-03-01</span> • [Basic coding in Python #2: Functions, methods & classes (PY2)](#PY2)
##### <span class="tab">2021-03-01</span> • [Sketching, feedback & planning in type design (TY4)](#TY4)
##### <span class="tab">2021-03-09/10</span> • [== Free workshop == Design Game Pentathlon 5 Rounds (DG1)](#DG1)
##### <span class="tab">2021-03-15</span> • [Coding advanced logo variations (LO2)](#LO2)
##### <span class="tab">2021-03-15</span> • [Scripting for RoboFont (PY5)](#PY5)
##### <span class="tab">2021-03-29</span> • [Basics of typography, grids & layout (GD1)](#GD1)
##### <span class="tab">2021-03-29</span> • [Coding simple scripted tools (PY3)](#PY3)

#### April
##### <span class="tab">2021-04-12</span> • [Coding tools with a user interface (PY4)](#PY4)
##### <span class="tab">2021-04-12</span> • [Coding advanced typography & layouts for print and web (GD2)](#GD2)
##### <span class="tab">2021-04-26</span> • [Design design spaces for Variable Fonts (TY6)](#TY6)
##### <span class="tab">2021-04-26</span> • [Visual grammar #1: The seven parameters of Bertin (VG1)](#VG1)

#### May
##### <span class="tab">2021-05-10</span> • [Visual grammar #2: Balance diversity & coherency (VG2)](#VG2)
##### <span class="tab">2021-05-10</span> • [Design the process and tools for Variable Fonts (TY7)](#TY7)
##### <span class="tab">2021-05-24</span> • [Selecting typefaces (GD3)](#GD3)
##### <span class="tab">2021-05-24</span> • [Teaching simulations and design games (DE2)](#DE2)

#### June
##### <span class="tab">2021-06-07</span> • [Coding type specimens (GD4)](#GD4)
##### <span class="tab">2021-06-07</span> • [Sketching type (TY3)](#TY3)
##### <span class="tab">2021-06-21</span> • [Coaching Type Projects (TY5)](#TY5)
##### <span class="tab">2021-06-21</span> • [Design and code info-graphics (IG1)](#IG1)

#### Julu
##### <span class="tab">2021-07-05</span> • [Designing a script (TY8)](#TY8)
##### <span class="tab">2021-07-05</span> • [Basic exhibition design (SD1)](#SD1)
##### <span class="tab">2021-07-19</span> • [Coding your spacing/kerning tool (TY9)](#TY9)
##### <span class="tab">2021-07-19</span> • [Workspace design (SD2)](#SD2)

~~~
box = section.newCropped()
~~~
![cover y=top](images/BNO-BuroBoek2008.png)


<-- W O R K S H O P  D E S C R I P T I O N S  -->




