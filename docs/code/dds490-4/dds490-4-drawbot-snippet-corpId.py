# Version 1.0
# DrawBot standard creates a canvas of 1000x1000 pt
# Set the fill color to white and draw the background.
fill(1)
rect(0, 0, 1000, 1000)
# drawbotsnippet smartass CorpID
W = 195 # Width of a page
l = 40 # Margins (padding) on the page
l2 = l/2 # Half margin
R = range(30,1000,W) # Range of page positions

def drawPage(x,y):
  w = W * 0.5 + random() * 80 # Random page size within range
  h = W * 0.4 + random() * 100
  stroke(None)# No stroke on the logo
  fill(1, 0, 0.5) # Magenta logo rectangle
  rect(x+l2, y+h-l2, l, l2)
  stroke(None) # No stroke around text
  fill(0.8) # Gray text column
  rect(x+l2, y+l2, w-l, h-l-l2)
  stroke(0) # Black stroke
  fill(None) # No fill
  rect(x, y, w, h)# Draw frame as last, so it covers bleed logo
  
for x in R: # All x positions of the layout
  for y in R: # All y positions of the layout
    drawPage(x,y) # Draw the page on (x,y) location
    
saveImage('dds490-4-corpid.png')
saveImage('dds490-4-corpid.svg')
