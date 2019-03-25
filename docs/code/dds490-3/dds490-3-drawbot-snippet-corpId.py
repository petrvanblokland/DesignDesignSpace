fill(1)
rect(0, 0, 1000, 1000)

#drawbotsnippet smartass CorpID
W,l=195,40
l2,n,f,s,r,R,c=l/2,None,fill,stroke,rect,range(30,1000,W),random
def p(x,y):
  w=W*0.5+c()*80
  h=W*0.4+c()*100
  s(0),f(n),r(x,y,w,h),
  f(0,10,1),r(x+l2,y+h-l2,l,l2),s(n),
  f(0.8),r(x+l2,y+l2,w-l,h-l-l2)
for x in R:
  for y in R:
    p(x,y) 
    
saveImage('dds490-3-corpid.png')
saveImage('dds490-3-corpid.svg')