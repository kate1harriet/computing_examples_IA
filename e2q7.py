
def function1(x):
    ret = x**3+x**2
    return ret

def first_diff1(x):
    ret = 3*x**2+2*x
    return ret

def second_diff1(x):
    ret = 6*x + 2
    return ret
    
tol = 1e-8

max_it = 50

def run(f, dfdx, d2fdx2, x0, tol, max_it):
    x = [x0]
    for it in range(max_it):
        while abs(dfdx(x[len(x)-1]))/abs(d2fdx2(x[0]))>tol:
            ret = x[len(x)-1] - dfdx(x[len(x)-1])/d2fdx2(x[len(x)-1])
            x.append(ret)
    return x[len(x)-1], f(x[len(x)-1]), len(x)
    
def function2(x):
    ret = x**2
    return ret

def first_diff2(x):
    ret = 2*x
    return ret

def second_diff2(x):
    ret = 2.0
    return ret

y = run(function1, first_diff1, second_diff1, 1, tol, max_it)
print(y)
z = run(function2, first_diff2, second_diff2, 1, tol, max_it)
print(z)

