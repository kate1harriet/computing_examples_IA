from sympy import *
import numpy as np
import math

"""
def function(x):
    x = Symbol('x')
    a = x*x
    b = a.diff(x)
    return a,b


def num_diff_1(f,x,h):
    a,b = f(x+h)
    c,d = f(x)
    ret = (a-c)/h
    return ret

def num_diff_2(f,x,h):
    a,b = f(x+h)
    c,d= f(x-h)
    ret = (a-c)/2*h
    return ret

def difference(f1,f2,x,h):
    a,b = f1(x)
    c= f2(f1,x,h)
    return (b-c)



h = 0.01
x = 1


print(difference(function, num_diff_1,x,h))
print(difference(function, num_diff_2,x,h))
"""

# This task should instead be completed with math.sin and math.cos functions
# Those with known derivatives, rather than generalised forms
# as a general rule, the symmetric difference will be of the order of magnitude
# of the non-symmetric difference squared


x = 1.2 
H = [1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4] 
for h in H: 
    one_side_diff = (math.sin(x + h)- math.sin(x))/h 
    symm_diff = (math.sin(x + h)- math.sin(x-h))/(2*h) 
    print("h =", h) 
    print(" One-side error: {:.2e}".format(abs(one_side_diff- math.cos(x)))) 
    print(" Symmetric error: {:.2e}".format(abs(symm_diff- math.cos(x))))





