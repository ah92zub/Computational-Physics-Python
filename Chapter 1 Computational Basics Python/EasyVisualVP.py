# EasyVisualVP.py

# import libraries
from vpython import *

# define graph window properties
graph1 = graph(align='left', height=400, width=600, background=color.white,
               foreground=color.black, title='2-D Plot', xtitle='x', ytitle='f(x)')

# define plot line properties
Plot1 = gcurve(color=color.red)

# plot the points one by one
for x in arange(0,8.1,0.1):
    Plot1.plot(pos=(x , 5*cos(2*x)*exp(-0.4*x)))

# define graph window properties
graph2 = graph(align='right', height=400, width=600, background=color.white,
               foreground=color.black, title='2-D Plot', xtitle='x', ytitle='f(x)')

# define plot line properties
Plot2 = gcurve(color=color.black)

# plot the points one by one
for x in arange(-5,5,0.1):
    Plot2.plot(pos=(x,cos(x)))
