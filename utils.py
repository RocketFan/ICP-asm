import numpy as np

def get_2D_R(rad):
    c, s = np.cos(rad), np.sin(rad)
    R = np.array([[c, -s, 0],
                  [s, c, 0],
                  [0, 0, 1]])

    return R

def get_2D_T(x, y):
    T = np.eye(3)
    T[:2, 2] = [x, y]

    return T

def get_2D_func(coefficients, bias=0):

    def _func(x):
        result = 0

        for i, c in enumerate(coefficients[::-1]):
            result += c * x ** i
        
        return result + bias

    return _func