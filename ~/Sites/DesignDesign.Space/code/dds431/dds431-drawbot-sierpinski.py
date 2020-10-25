#drawbotsnippet Sierpinski
def sierpinskiSquare(X, Y, w, c):
  if w > 1: # Recursion limit
    for i in range(3): # For all rows
      for j in range(3): # For all columns
        px, py = X + i * w, Y + j * w
        if (i, j) == (1, 1):
          fill(c) # Draw middle as rect or oval.
          choice((rect, oval))(px, py, w, w)
        else: # Recursively repeat all
          sierpinskiSquare(px, py, w/3, c * 0.8)
# Main call for the entire image.          
sierpinskiSquare(0,0,1000/3,0.9)

saveImage('dds431-sierpinski-square.png')
# Note that SVG is not efficient here, too large for web.
saveImage('dds431-sierpinski-square.svg') 
