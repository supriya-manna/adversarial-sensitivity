#Thanks to Dr. Escobedo for sharing the code of tauX_hat from his paper: https://doi.org/10.1016/j.ejor.2020.02.027
from itertools import product
from functools import reduce
import time
from math import ceil
from numpy import *

def printMatrix(A):
    #Takes a list of lists and prints them out line by line
    for i in range(len(A)):
        print(A[i])


def getScoreMatrix(a):
    #Takes a ranking vector (list) a, and returns a score matrix (list of lists) corresponding to it

    #Create an nxn matrix
    matrix = []
    for i in range(len(a)):
        matrix.append([None]*len(a))

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j or a[i] == 0 or a[j] == 0:
                matrix[i][j] = 0
            elif a[i] <= a[j]:
                matrix[i][j] = 1
            else:
                matrix[i][j] = -1

    return matrix


def tauX(a,b):
    #Takes two vectors a, b and returns the correlation coefficient Tau-x between them
    A = getScoreMatrix(a)
    B = getScoreMatrix(b)
    total = 0
    for i in range(len(A)):
        for j in range(len(A)):
            total += A[i][j]*B[i][j]
    tau = total/(len(A)*(len(A)-1))

    return tau

def tauX_hat(a,b):
    #Takes two vectors, a and b, and returns the extended corr. coef. Tau-x-e between them
    A = getScoreMatrix(a)
    B = getScoreMatrix(b)
    total = 0
    common = 0
    for i in range(len(a)):
        if a[i] != 0 and b[i] != 0:
            common += 1
    for i in range((len(A))):
        for j in range(len(A)):
            total += A[i][j]*B[i][j]
    tau = total/(common*(common-1))

    return tau
