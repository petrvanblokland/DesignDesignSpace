# Day 1: From bare page to photobook

The focus of day 1 is in creating a bare page with some content, some measurements, a document with multiple pages and an animation.
The subfocus is to become aware of transforming values (e.g. a position) into relations and algorythms. (e.g instead defining two horizontal positions x1 = 100; y1 = 200; we write x1 = 100; x2 = 2 * x1) 

## A photobook

Let's focus on making a photobook today, this could be the brief from your customer:

* There is an existing folder with images (could be offered by your customer, make one with 10-30 photo’s of yourself. The amount is arbitrary, but don’t start with too many, to make the test-runs fast)
* Automate the building of a single photobook document with as many pages as there are photo's 
* Each page contains one photo and its file name as title. 
* The width of the photo fits the width of the page inside the margin/padding white around it.
* If the restulting height exceeds the available space, then the size is scaled down until it fits. 
* The title/file name is positioned below the photo.
* Export as PDF and a animated gif (with a frame time of 2 seconds).

As you can see, even a relative small automation assignment needs breaking into smaller pieces, so you can build up your day schedule. 
This is a suggested set of smaller assignments. 

(Different from what we did yesterday: skip the canvas position. The document will have the same size as our page, so that reduces the complexity a bit. I should have done that from the beginning. I'll update the document of yesterday to that more simple approach, add comments explaining what we did.)

* Make a PDF document with one page of a defined size. Add a color square somewhere on the page.
* Make a PDF document with multiple pages of a defined size. Add a color square on each page with a random color and a random position (while making sure that the square always stays inside margin/padding boundaries.
* Add a line of text below the square, left aligned.
* Center the text under the square
* Make the square randomly vary in width/height ratio (within limitation, e.g. max difference of 2:3), while making sure that all of the above remain working.
* Fit the rectangle on the available width in the page.
* Replace the rectangle by an image.
* Run through the folder of images to create a page for each image.
* Save as PDF
* Save as animated gif, with 2 seconds interval between the slides.

Not all of the above can be solved with what we address yesterday, but let's see how far you get. I will give hints on specific questions. 