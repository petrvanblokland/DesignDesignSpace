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

# Start your study project in 2025 (or maybe this year)



~~~
from pagebot.constants import *
slideshow = content.newSlideShow(h=300, slideW='100%', slideH=300, startIndex=3, autoHeight=True, carousel=2, dynamicHeight=False, transition='slide', easing=CSS_EASE, frameDuration=4, duration=0.7, pauseOnHit=True, randomPlay=False)
box = slideshow.slides
~~~

![Sketched letters cover y=center](images/IMG_2848.jpg)
![Writing material makes contrast in type x=center y=center](images/IMG_1108.jpg)
![Upgrade_in_use_05_meeting room x=center y=center](images/typetr/Upgrade_in_use_05_meeting_room.jpg)
![Bitcount in use x=center y=center](images/typetr/Bitcount_in_use_03_time_is_now3.jpg)
![Blue Orange cloth cover y=top x=center](images/IMG_3145.jpg)
![Powerlift_in_use_06_retrofuturism x=center y=top](images/typetr/Powerlift_in_use_06_retrofuturism.jpg)
![Color squares cover y=top x=center](images/PepperTomColorSquares.png)
![Upgrade_in_use_08_Keep_calm x=center y=center](images/typetr/Upgrade_in_use_08_Keep_calm.jpg)
![White painted grid cover y=top x=center](images/IMG_1107.jpg)
![G-Cube variables cover y=center x=center](images/GN-Cube-Variable-e.png)
![Collage Coffee pot and textile y=top x=center](images/IMG_6704.jpg)
![PPowerlift_in_use_07_SSSH x=center y=top](images/typetr/Powerlift_in_use_07_SSSH.jpg)
![Theme colors cover y=top x=center](images/ThemeColorsByDocument_5.png)
![Sketched toys cover y=top x=center](images/IMG_4905.jpg)
![Presti_in_use_06_Chocolate heaven_neon x=center y=center](images/typetr/Presti_in_use_06_Chocolate_heaven_neon.jpg)
![DrawBotHomePage cover y=top x=center](images/DrawBotHomePage.png)
![Presti_in_use_08_buddha_cat_sits x=center y=center](images/typetr/Presti_in_use_08_buddha_cat_sits.jpg)
![Model interior cover y=center x=left](images/IMG_E8927.jpg)
![Affiche Rituelen cover y=bottom x=center](images/affiche_rituelen.png)
![Sketching details cover y=top x=center](images/DesignModels2.038.png)
![Proforma_in_use_04_things to forget4 x=center y=center](images/typetr/Proforma_in_use_04_things_to_forget4.jpg)
![Shells on green wood cover y=top x=center](images/IMG_0752.jpg)
![Triangle pattern cover y=bottom x=center](images/IMG_1447.jpg)
![Interior sketch cover y=top x=center](images/IMG_E8874.jpg)
![Upgrade_in_use_02a x=center y=center](images/typetr/Upgrade_in_use_02a.jpg)
![Corner write-black-green cover y=top x=center](images/IMG_6994.jpg)
![Den Bosch letter door cover y=top x=center](images/IMG_6129.jpg)

~~~ 
box = slideshow.side
~~~

# Develop your process. Expand your skills.

* Projects on “Master” level
* Tell us your interests
* Define your own tempo
* What fits your budget?
* Exercises and feedback

# [Contact us](mailto:info@designdesign.space?subject=Subscribing%20for%20the%20free%20DesignDesign.Space%20workshop)


~~~
box = content.newIntroduction()
~~~

# Working from home? Studying online in post-Corona world? Define a project you would like to do, but cannot find a way to start. Develop your profession. 

~~~ 
#box = section.newCropped()
## ![Sponsoring Typographics2020]()
#![Typographics2020Logo.png x=center y=center](images/Typographics2020Logo.png)
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Studying at DD.S: what is it like?

* Intensive exercises and daily personal feedback;
* The result of the exercises is shared on a closed Slack channel for the duration of the study;
* Feedback comes from the educators and the other students;
* DesignDesign.Space offers a safe online study environment, where any question can be asked;
* Tell us what your budget is.

~~~
box = section.newCropped()
~~~
![cover y=top x=center](images/DSGNWK_0665BW.jpg)

