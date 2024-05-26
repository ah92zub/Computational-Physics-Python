# import Libraries
import numpy as np
from .NumericalDiff import central_diff

# bisection algorithm
def bisection(func, x_minus, x_plus, N, eps):
    x_hist = []
    for _ in range(N):
        x = (x_minus + x_plus)/2
        if func(x_plus)*func(x) > 0:
            x_plus = x
        else:
            x_minus = x
        if abs(func(x)- 0) < eps:
            break
        x_hist.append(x)
    return x, x_hist

# newton raphson method
def newtonraphson(func, x_o, N, eps):
    x_hist = [x_o]
    x = x_o
    for _ in range(N):
        if abs(central_diff(func, x, eps)) < eps:
            print('Error')
        else:
            delta_x = -(func(x)/central_diff(func, x, eps))
            x = x + delta_x
            x_hist.append(x)
            if abs(func(x) - 0) < eps:
                break    
    return x, x_hist  
