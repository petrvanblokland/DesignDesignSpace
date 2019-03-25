
~~~
# ----------------------------------------
# Scales:design education
# ----------------------------------------
template = doc.getTemplate('home')
page = page.next
page.applyTemplate(template)  
page.name = 'Design education'
page.url = 'Scales/design_education_700.html'

content = page.select('Content')
box = content.newBanner()
~~~
# [Scales:](scales.html) Design education

~~~
box = content.newIntroduction()
~~~
# Teaching design students? Educating customers? Planning ahead for research? Preparing a presentation? 
~~~
section = content.newSection()
box = mainBox = section.newMain()
~~~
<a name="Scale730"/>
## Educating grid design for print^730
Write a script (DrawBot or PageBot) that generates variations of grids for print. Use them in an educational context by adding comments in the code that explain how it works. Design a method to validate the result with a group. **1 day**

~~~
section = content.newSection()
box = mainBox = section.newMain()
~~~
<a name="Scale731"/>
## Educating grid design for web^731
Write a script (DrawBot or PageBot) that generates variations of grids for HTML/CSS. Use them in an educational context by adding comments in the code that explain how it works. Design a method to validate the result with a group. **1 day**

~~~
section = content.newSection()
box = mainBox = section.newMain()
~~~
<a name="Scale760"/>
## Make students sketch out a timeline for their career^760

What medium would you choose? What iterations would you go through? What would the students present at then end of the day? And how could the results be verified to some extend? Who did best of the group? **1 day** 

~~~
section = content.newSection()
box = mainBox = section.newMain()
~~~
<a name="Scale790"/>
## Design a workshop about Graphic Design^790

Sketch a 5-day workshop addressing the profession of Graphic Design. What skills and knowledge should students get to be a designer for the rest of their professional lives? Also design a method for feedback: how good is your workshop? **3 hours**

