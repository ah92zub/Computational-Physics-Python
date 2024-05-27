# import libraries
import numpy as np
import numpy.linalg as la

# define the linear least saquares model
def leastsquares(x: np.ndarray, y: np.ndarray, sigma_squared: np.ndarray, order_model: int ) -> np.ndarray:
    num_coeffs = order_model + 1
    data_points = len(x)
    S_x = np.zeros((num_coeffs,num_coeffs), float)
    b_xy = np.zeros(num_coeffs, float)
    # S_x matrix
    for indx, _ in np.ndenumerate(S_x):
        S_x[indx] = np.sum(x**np.sum(indx)/sigma_squared)
    # b_xy vector 
    for indx, _ in np.ndenumerate(b_xy):
        b_xy[indx] = np.sum((x**indx)*y/sigma_squared)
    return la.solve(S_x, b_xy)


# define the Vandermonde Matrix
def vandermonde(x: np.ndarray, order_model: int) -> np.ndarray:
    num_coeffs = order_model + 1
    Vandermonde = np.ones((len(x),num_coeffs ), float)
    for indx in range(1,num_coeffs):
        Vandermonde[:,indx] = np.transpose(x**indx)
    return Vandermonde
