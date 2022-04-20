import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, num = 50)
y = []
z = [0]

def function(x):
    ret = (np.sin(x)+np.cos(10*x))/5
    return ret

for i in x:
    y.append(function(i))


for i in range(1,49):
    ret = (y[i-1]+y[i]+y[i+1])/3
    z.append(ret)

z.append(0)

plt.plot(x, y, label = 'exact')
plt.plot(x,z, label = 'averaged')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.figure()
plt.show()

