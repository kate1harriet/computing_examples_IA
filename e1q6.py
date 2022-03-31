import math

#initial function
def function(x):
    f = x**3 +x**2
    return f

#main function, uses lists to iterate through sum
def numerical_integration(a,b,w,x):
    ret = 0
    for i in range(len(w)):
        ret += (b-a)*function(x[i])*w[i]
    return ret

def error(real_ret, run):
    ret = (real_ret-run)*100/real_ret
    return ret


#run for trapezoidal rule
a=0
b=10
real_ret = 8500/3
w1=[0.5,0.5]
x1=[a,b]
run1 = numerical_integration(a,b,w1,x1)
print('Trapezoidal rule result:',run1)
accuracy1 = error(real_ret, run1)
print('Trapezoidal rule error:', accuracy1)

#run for simpson's rule
w2=[1/6, 2/3, 1/6]
x2=[a, (a+b)/2, b]
run2 = numerical_integration(a,b,w2,x2)
print('Simpsons rule result:',run2)
accuracy2 = error(real_ret, run2)
print('Simpsons rule error:', accuracy2)

#run for gauss quadrature
w3=[0.5, 0.5]
x3=[((a+b)/2+(b-a)/(2*math.sqrt(3))), ((a+b)/2-(b-a)/(2*math.sqrt(3)))]
run3 = numerical_integration(a,b,w3,x3)
print('Gauss rule result:',run3)
accuracy3 = error(real_ret, run3)
print('Gauss rule error:', accuracy3)
