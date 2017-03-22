from __future__ import division
import numpy as np
def gauss_elimination(a, b):
    n = len(b)
    x = [None] * n
    a = a.astype(float)
    b = b.astype(float)
    print x
    for i in range(0, n - 1):
       for j in range(i + 1, n):
             if a[j, i] != 0:
                lmd = a[j, i] / a[i, i]
                a[j, i:n] -= lmd * a[i,i:n] 
                b[j] -= lmd * b[i]
    for i in range(n - 1, -1, -1):
        x[i] = ((b[i] - np.dot(a[i, i + 1 : n], x[i + 1: n])) / a[i, i])
        
    return (a, x)

def init():
    a = np.array([(4,-2,1),(-2,4,-2),(1,-2,4)])
    b = np.array([11,-16,17])
    x = gauss_elimination(a, b)
    print x

init()
                
