import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

MAX_ITER = 100

def f(x):
    return pow(x, 3) - x - 2 
    #return lambda x: np.cos(x) - x

def falsaPosicao(a, b):
    resultado = None
    if (f(a) * f(b) < 0):
        for i in range(MAX_ITER):
            fa = f(a)
            fb = f(b)

            xr = b - ((fb * (a - b)) / (fa - fb))

            if abs(f(xr)) < pow(10, -5):
                break
            
            if fa * f(xr) < 0:
                b = xr
            
            elif fb * f(xr) < 0:
                a = xr
        resultado = xr

    print(xr)
    return True

falsaPosicao(1, 2)