from __future__ import division
import numpy as np

def cofactor(i, j, matrix) : 
    return ((-1) ** (i + j)) * minor(i, j, matrix)


def two_by_two(matrix) :
    return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1,0]

def minor(i, j, matrix) :
    matrix = np.delete(matrix, i, 0)
    matrix = np.delete(matrix, j, 1)
    if len(matrix[0]) == 2:
        return two_by_two(matrix)
    else :
        return determinant(matrix)
        
def determinant(matrix) :
    n = len(matrix[0])
    if n == 2 :
        return two_by_two(matrix)
    i = 0
    determinant = 0;
    for j in range(0, n) :
        determinant += cofactor(i, j, matrix) * matrix[i, j]
    return determinant

def is_singular(matrix) :
    det = determinant(matrix)
    if(det == 0) :
        return True
    else :
        return False

def init() :
    a = np.array([(2,1,3),(1,0,2),(2,0,-2)])
    b = np.array([(1,3),(2,6)])
    print is_singular(a)
    print is_singular(b)



init()
