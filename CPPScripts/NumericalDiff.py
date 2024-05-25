# first order numerical differentiation 

# import libraries
import numpy as np


# forward difference
def forward_diff(f: np.ufunc, x: float, step_size: float) -> float:
    return (f(x+step_size) - f(x))/step_size
# central difference
def central_diff(f: np.ufunc, x: float, step_size: float) -> float:
    return (f(x+step_size/2) - f(x-step_size/2))/step_size