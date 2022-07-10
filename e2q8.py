## Q7, but modified syntax to create amd initialise a class
# then the function need to be modified so that it calls from the class
import numpy as np

class Rosenbrock:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def f(self,x):
        return (self.a - x[0])**2+self.b*(x[1]-x[0]**2)**2

    def g(self,x):
        return np.array([-2*self.a-x[0]-4*x[0]*self.b*(x[1]-x[0]**2), 2*self.b*(x[1]-x[0]**2)])

    def J(self,x):
        d2f_dx2 = 2- 4*self.b*(x[1]-x[0]**2)+8*self.b*x[0]**2
        d2f_dxdy = -4*self.b*x[0]
        d2f_dy2 = 2*self.b
        return np.array([[d2f_dx2, d2f_dxdy],[d2f_dxdy, d2f_dy2]])
        