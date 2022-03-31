import numpy as np
import random
import math

def f(x,y):
    ret = math.exp(x*y)*math.cos(y)*math.cos(y)*math.sin(x**2)
    return ret

def pi_approx(x,y):
    if x*x+y*y <1:
        return 1
    else:
        return 0

def mean(f, N,a,b):
    sum=0
    for i in range(N):
        xtest = random.uniform(-a, a)
        ytest = random.uniform(-b,b)
        sum += f(xtest, ytest)
    return sum*(4*a*b)/N

a=1
b=1
N=1000000

run = mean(f,N,a,b)
print('mean value approximation is:' , run)


run_pi = mean(pi_approx, N,a,b)
print('Pi approximation is:', run_pi)