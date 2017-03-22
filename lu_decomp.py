from __future__ import division
import numpy as np


def lu_decomp(a):
    n = len(a)
    a = a.astype(float)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[j, i] != 0:
                lmd = a[j, i] / a[i, i]
                a[j, i + 1:n] -= lmd * a[i, i + 1:n]
                a[j, i] = lmd
    return a

def lu_solve(a, b):
    n = len(b)
    b = b.astype(float)
    for i in range(1, n):
        b[i] = b[i] - np.dot(a[i,0:i], b[0:i])
    for i in range(n - 1, -1, -1):
        b[i] = (b[i] - np.dot(a[i, i + 1:n],b[i + 1:n])) / a[i, i]
    return b

def init():
    a = np.array([(4,-2,1),(-2,4,-2),(1,-2,4)])
    b = np.array([11,-16,17])
    a = lu_decomp(a)
    b = lu_solve(a, b)
    print a
    print b


init()
                
