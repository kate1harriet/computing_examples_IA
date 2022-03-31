
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def calc(x0,x1, tmin, tmax, deltaT,m,k,f):
    x=[x0,x1]
    t=[tmin, tmin+deltaT]
    it = int((tmax-tmin)/deltaT)
    #compute the actual x(n+1) calc and add to list
    for i in range(it-2):
        newX = (f/m)*deltaT**2+x[i+1]*(2-(k/m)*deltaT**2)-x[i]
        x.append(newX)
        t.append(tmin+(i+2)*deltaT)
    return x,t

#initial conditions for analytical solution
x0=0.01
x1=0.01
tmin=0
tmax=20
deltaT = 0.01
m=1
k=40
f=0

# Exact solution
T = np.arange(0, 20, deltaT)
w = np.sqrt(k/m)
x_exact = 0.01*np.cos(w*T)

#adjusting initial conditions to include a variable f value
def signF(f,v):
    if v>0:
        return -f
    if v<0:
        return f
    else:
        return 0

f2 = 0.025
xnew=[x0,x1]

for n in range(2, len(T)):
    # Compute (approximate) velocity (used to determine friction force)
    v = (xnew[n-1] - xnew[n-2])/deltaT
    # Compute x_n
    ret = (deltaT*deltaT/m)*signF(f2,v) - (deltaT*deltaT*k/m)*xnew[n-1] + 2*xnew[n-1] - xnew[n-2]
    xnew.append(ret)


x,t = calc(x0,x1,tmin,tmax,deltaT,m,k,f)
plt.plot(t, x, label = 'numerical')
plt.plot(t,x_exact, label = 'analytical')
plt.plot(t, xnew, label = 'damped')
plt.xlabel('$t$')
plt.ylabel('$x$')
plt.legend()
plt.figure()
plt.show()



