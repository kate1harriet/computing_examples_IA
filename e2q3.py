from sympy import *
import numpy as np
import math

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


# This task should instead be completed with math.sin and math.cos functions
# Those with known derivatives, rather than generalised forms
# as a general rule, the symmetric difference will be of the order of magnitude
# of the non-symmetric difference squared






