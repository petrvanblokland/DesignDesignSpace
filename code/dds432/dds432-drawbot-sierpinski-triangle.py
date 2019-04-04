
if 1: # Some sizing. Tweak for other sizes.
    SIZE = 33 # Size of vertex in cubes
    LIMIT = 5 # Recursive limit where the cubes are drawn.
    dx, dy = 25.5, 25 # Width/height ratio cubes
    ox, oy = 4, 3 # Origin on canvas.

elif 0: # Large one. Tweak for other sizes.
    SIZE = 65 # Size of vertex in cubes
    LIMIT = 9 # Recursive limit where the cubes are drawn.
    dx, dy = 13, 12 # Width/height ratio cubes
    ox, oy = 8, 6 # Origin on canvas.

else: # Small one. Tweak for other sizes.
    SIZE = 17 # Size of vertex in cubes
    LIMIT = 5 # Recursive limit where the cubes are drawn.
    dx, dy = 51, 50 # Width/height ratio cubes
    ox, oy = 2, 1.5 # Origin on canvas.
       
# Original colors of example.
c0 = 0x65/255, 0x65/255, 0x99/255
c1 = 0x99/255, 0x99/255, 0xBF/255
c2 = 0xC8/255, 0xC8/255, 0xD9/255
whiteColor = 0xE9/255, 0xE9/255, 0xFA/255 # Hilight lines.
blackColor = 0.1, 0.1, 0.1 # Rib color of not hilight.
noColor = None, None, None

paths = {} # Sorting path in vison order  

def addPath(v, path, fillColor, strokeColor):
    if not v in paths:
        paths[v] = []
    paths[v].append((path, fillColor, strokeColor))
    
def drawCube(x, y, t, n, side, nn):
    # Draw the cube as 3 paths and 2 hilights.
    # Check on position in the rectangle to guess the sorting order.
    v = 100
    if nn == 30: 
        v = -1
    elif t == 300 and n == 0:
        v = -1
    elif 1 and t == 100 and nn == 20 and n == side-1:
        v = -1
    elif 1 and t == 100 and nn == 20 and n == side-2:
        v -= 10
    path = BezierPath() # Left
    path.moveTo((x*dx, y*dy))
    path.lineTo((x*dx, (y+1)*dy))
    path.lineTo(((x-1)*dx, (y+1.5)*dy))
    path.lineTo(((x-1)*dx, (y+0.5)*dy))
    path.lineTo((x*dx, y*dy))
    path.closePath()
    addPath(v, path, c0, blackColor)

    v = 0
    if nn == 10 and n == 1:
        v = 20
    elif nn == 30 and n == side-2:
        v = 150
    path = BezierPath() # Right
    path.moveTo((x*dx, y*dy))
    path.lineTo((x*dx, (y+1)*dy))
    path.lineTo(((x+1)*dx, (y+1.5)*dy))
    path.lineTo(((x+1)*dx, (y+0.5)*dy))
    path.lineTo((x*dx, y*dy))
    path.closePath()
    addPath(v, path, c1, blackColor)

    # Add hilights if visible
    if nn == 10 and n > 0 and n < side-1:
        path = BezierPath() # Vertical hightlight
        path.moveTo((x*dx, y*dy+1))
        path.lineTo((x*dx, (y+1)*dy-1))
        path.closePath()
        addPath(v+100, path, whiteColor, whiteColor)
            
    if nn == 30 and n > 0 and n < side-1:
        path = BezierPath() # Vertical hightlight
        path.moveTo((x*dx+1, (y+1)*dy+dy/2/dx))
        path.lineTo(((x+1)*dx-1, (y+1.5)*dy-dy/2/dx))
        path.closePath()
        addPath(v+200, path, whiteColor, whiteColor)
        
    v = 0
    if nn == 20 and n == 1:
        v = 50
    elif nn == 30 and n == side-2:
        v = 300
    path = BezierPath() # Top
    path.moveTo((x*dx, (y+1)*dy))
    path.lineTo(((x-1)*dx, (y+1.5)*dy))
    path.lineTo((x*dx, (y+2)*dy))
    path.lineTo(((x+1)*dx, (y+1.5)*dy))
    path.lineTo((x*dx, (y+1)*dy))
    path.closePath()
    addPath(v, path, c2, blackColor)
  
def drawTriangle(x, y, side, t):
    # Draw the cube as 3 paths, and sort them in drawing order.
    for n in range(int(side)):
        fill(0.5)
        drawCube(ox+x, oy+y+n, t, n, side, 10)
        drawCube(ox+x+n, oy+y+side-n/2-1, t, n, side, 20)
        drawCube(ox+x+n, oy+y+n/2, t, n, side, 30)
            
def SierpinskiTriangle(x, y, side, t=0):
    # Recursibe triangle drawing
    if side > LIMIT:
        newSide = (side - 1)/2 + 1 
        SierpinskiTriangle(x, y, newSide, t=100)
        SierpinskiTriangle(x, y + newSide-1, newSide, t=200)
        SierpinskiTriangle(x + newSide-1, y + newSide/2-0.5, newSide, t=300)
    else:
        drawTriangle(x, y, side, t)

SierpinskiTriangle(0, 0, SIZE)

# Now all paths are drawn, sort them by visible order
# and the draw them in their colors.
# This also includess the hilight lines as path,
for v, pathColors in sorted(paths.items()):
    if v < 0:
        continue
    for path, (fr, fg, fb), (sr, sg, sb)  in pathColors:
        stroke(sr, sg, sb)
        strokeWidth(1.5)
        miterLimit(1)
        if fr is None:
            fill(None)
        else:
            fill(fr, fg, fb)
        drawPath(path)
 
# Save as PNG and PDF      
saveImage('SierpinskyTriangle%d.png' % SIZE)
saveImage('SierpinskyTriangle%d.pdf' % SIZE)

