import math
import numpy as np

x = [10,100,1000,10000]
h = [1e-9, 1e-12, 1e-15]

def function(x):
    ret = x**2*np.sin(x*x)
    return ret

def derivative(x):
    ret = 2*x*np.sin(x*x)+2*x**3*np.cos(x*x)
    return ret


def complex_step(f,x,h):
    y = f(x+h*1j)
    ret = np.imag(y)/h
    return ret

for x in x:
    for k in range(len(h)):
        print('For X is equal to', x, ', and H is equal to', h[k], ', the error is:')
        a = derivative(x)
        b = complex_step(function, x, h[k])
        print(abs(a-b))

