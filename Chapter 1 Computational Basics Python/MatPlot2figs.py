# MatPlot2figs.py : plot subfigs

# import libraries
import pylab as p
import numpy as np

# define plot parameters
Xmin = -5.0
Xmax = 5.0
Npoints = 500

DelX = (Xmax - Xmin)/Npoints
x1 = np.arange(Xmin, Xmax, DelX)
x2 = np.arange(Xmin, Xmax, DelX/20)

# define the plot functions 
y1 = -np.sin(x1)*np.cos(x1**2)
y2 = np.exp(-x2/4.0)*np.sin(x2)

# figure 1 subplot 1
p.figure(1)
p.subplot(2, 1, 1)
p.plot(x1, y1, 'r', lw=2)
p.xlabel('x')
p.ylabel('f(x)')
p.subplot(2, 1, 1).set_title('$-\sin(x)*\cos(x^2)$')
p.grid(True)

# figure 1 subplot 2
p.subplot(2, 1, 2)
p.plot(x2, y2, '-', lw=2)
p.xlabel('x')
p.ylabel('f(x)')
p.subplot(2, 1, 2).set_title('$exp(-x/4)*sin(x)$')

# figure 2 subplot 1
p.figure(2)
p.subplot(2, 1, 1)
p.plot(x1, y1*y1, 'r', lw=2)
p.xlabel('x')
p.ylabel('f(x)')
p.subplot(2, 1, 1).set_title('$-\sin^2(x)*\cos^2(x^2)$')
p.grid(True)

# figure 2 subplot 2
p.subplot(2, 1, 2)
p.plot(x2, y2*y2, '-', lw=2)
p.xlabel('x')
p.ylabel('f(x)')
p.subplot(2, 1, 2).set_title('$exp(-x/2)*sin^2(x)$')


# display plot
p.show()
