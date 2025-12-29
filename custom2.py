#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:48:42 2025

@author: apple
"""
import numpy as np
import math
from nsymgen import*
################################################################################
def custom2(d, n, n1):
    h = 0
    v = 0
    e = 2**(n) - 1
    c = 2**(n-1)
    B, x = nsymgen(d,n)
    B = np.transpose(B)
    a = int(math.log(x, 2))
    for j in range (1, x):
        b = np.transpose(np.array([int(i) for i in bin(j)[2:].zfill(a)], dtype = int))
        d = np.mod(np.matmul(B, b), 2)
        s = d.sum()
        if s == c:
            v = v+1
            print(v)
            if h == 0:
                A = d
                h = 1
            else:
                A = np.vstack((A, d))
                p, q = A.shape
                print(p,q)
        if v == n1:
            break
    A = np.transpose(A)
    #B = np.ones( (e, n1), dtype = int )
    #C = 2*A - B
    return A

#########################################################################################
