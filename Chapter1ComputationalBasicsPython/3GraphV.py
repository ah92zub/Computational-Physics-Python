# 3GraphV.py : Vpython package, 3 plots bar, dot and curve

# import libraries
from vpython import *

string = 'blue : sin^2(x) , black : cos^2(x) , cyan : sin(x)*cos(x)'

# define graph window properties
graph1 = graph(title=string, xtitle='x', ytitle='f(x)', background=color.white,
               foreground=color.black)

# define plot curve properties
y1 = gcurve(color=color.blue)
y2 = gvbars(color=color.black)
y3 = gdots(color=color.cyan)

# plot the points
for x in arange(-5,5,0.1):
    y1.plot(pos=(x, sin(x)**2))
    y2.plot(pos=(x, cos(x)**2))
    y3.plot(pos=(x, sin(x)*cos(x)))