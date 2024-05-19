# GradeMatPlot.py : Matplotlib multi data sets

# import libraries
import pylab as p
import numpy as np

# Labels and titles
p.title('Grade Inflation')
p.xlabel('Years in College')
p.ylabel('GPA')

# plot the straight line at y=0
xa = np.array([-1, 5])
ya = np.array([0, 0])
p.plot(xa, ya)

# plot data 0
x0 = np.arange(0, 5, 1)
y0 = np.array([-1.4, 1.1, 2.2, 3.3, 4.0])
p.plot(x0, y0, 'bo')
p.plot(x0, y0, 'g')

# plot data 1
x1 = np.arange(0, 5, 1)
y1 = np.array([4.0, 2.7, -1.8, -0.9, 2.6])
p.plot(x1, y1, 'r')

# plot asymmetric error bars
errTop = np.array([1.0, 0.3, 1.2, 0.4, 0.1])
errBot = np.array([2.0, 0.6, 2.3, 1.8, 0.4])
p.errorbar(x1, y1, [errBot, errTop], fmt='o')

# plot grid lines
p.grid(True)

# display plot
p.show()