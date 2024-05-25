# numerical integration

# import libraries
import numpy as np

# Trapezoidal Approximation
def Integrate_Trapezoidal(func: np.ufunc, a: float, b: float, N: int) -> float:
    h = (b - a)/(N - 1)
    # define time vector
    t = np.linspace(a,b,N)
    # define the Trapezoidal weights
    w = h*np.ones(N)
    w[0] = w[0]/2
    w[-1] = w[-1]/2
    # calculate the integral
    return np.dot(w, func(t))

# simpson approximation
def Integrate_Simpson(func: np.ufunc, a: float, b: float, N: int) -> float:
    h = (b - a)/(N - 1)
    # define time vector
    t = np.linspace(a,b,N)
    # define the Simpson Weights 
    w = np.ones(N)
    w[1:(N-1):2] = 4
    w[2:(N-2):2] = 2
    w[0] = w[0]/2
    w[-1] = w[-1]/2
    w = (h/3)*w
    # calculate the integral
    return np.dot(w, func(t))

# Monte carlo integration
def Integrate_MonteCarlo(func: np.ufunc, a: float, b: float, N: int) -> float:
    t = (b-a)*np.random.rand(N) + a
    return np.sum(func(t))*((b-a)/N)