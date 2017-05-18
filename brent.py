from math import log, ceil

def root_search(f, start, dx, end):
    roots = [];
    while start <= end:
        temp = start + dx
        if f(temp) * f(start) < 0:
            roots.append((start, temp))
        start = temp
    return roots


def bisection(f, x1, x2, switch = 1, tol = 1.0e-9):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if f1*f2 > 0.0:
        print "Root is not bracketed!"
        return None
    n = ceil(log(abs(x2 - x1) / tol) / log(2.0))
    for i in range(int(n)):
        x3 = (x1 + x2) / 2.0
        f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) \
                and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if f2 * f3 < 0.0:
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3
    return (x1 + x2) / 2.0

def secant(f, x1, x2, tol = 1.0e-9, Max = 1000):
    f1 = f(x1)
    if f1 == 0:
        return x1
    f2 = f(x2)
    if f2 == 0:
        return x2
    for i in range(Max):
        x3 = x2 - f2 * (x2 - x1) / (f2 - f1)
        if abs(x3 - x2) < tol:
            return x3
        else:
            x1 = x2
            f1 = f2
            x2 = x3
            f2 = f(x3)
def swap(a, b):
    return (b, a)

def brent(f, x1, x2, tol =  1.0e-9):
    f1 = f(x1)
    f2 = f(x2)
    if f1 * f2 >= 0.0:
        print "Not bracketed!"
        return None
    if abs(f1) < abs(f2):
        x1, x2 = swap(x1, x2)
        f1, f2 = swap(f1, f2)
    x3 = x1
    f3 = f(x3)
    s = -1
    mflag = True
    while f2 != 0.0 and f(s) != 0.0 and abs(x2 - x1) > tol:
        if f1 != f3 and f2 != f3:
            s = (x1 * f2 * f3) / ((f1 - f2) * (f1 -f3)) + \
                (x2 * f1 * f3) / ((f2 - f1) * (f2 - f3)) + \
                (x3 * f1 * f2) / ((f3 - f1) * (f3 - f2))
        else:
            s = x2 - f2 * (x2 - x1) / (f2 - f1) 
        
        if s >= (3 * x1 + x2) / 4 and s <= x2 or \
           mflag and abs(s - x2) >= abs(x2 - x3) / 2 or \
           not mflag and abs(s - x3) >= abs(x3 - x4) / 2 or \
           mflag and abs(x2 - x3) < abs(tol) or \
           not mflag and abs(x3 - x4) < abs(tol):
            s = (x1 + x2) / 2.0
            mflag = True
        else:
            mflag = False
        fs = f(s)
        x4 = x3
        x3 = x2
        f3 = f2
        if f1 * fs < 0:
            x2 = s
            f2 = fs
        else:
            x1 = s
            f1 = fs
        if abs(f1) < abs(f2):
            swap(x1, x2)
            swap(f1, f2)
    return s
def func1(x):
    return x*x*x - 10*x*x + 5

def func2(x):
    return x*x -2

def func3(x):
        return x*x*x*x - 6.4*x*x*x + 6.45*x*x + 20.538*x - 31.752

def init(f, start, dx, num):
    brackets = root_search(f, start, dx, num)
    index = 0
    for a, b in brackets:
        x = brent(f, a, b)
        print "Root " + repr(index) + " is " + repr(x)
        index += 1
    print ""

init(func1, -10, 0.2, 10)
init(func2, -2, 0.1, 2)
init(func3, -2, 0.01, 5)
print "In third function, a double root could not be detected by " \
"the root search algorithm."
