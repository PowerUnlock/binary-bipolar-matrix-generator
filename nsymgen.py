# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:03:23 2022

@author: asus
"""
import numpy as np
import math
from nsymmetric import*
#################################################################################
def nsymgen(d,n):
    x, u = nsymmetric(d, n)
    a = 2**n - 1
    b = a - len(u)
    u = [0]*b+u
    B = np.array(u, dtype = int)
    C = np.array(u , dtype = int)
    for i in range (1, b+1):
        D = np.roll(C, - i)
        B = np.vstack((B, D))
    return(B, x)
    
    
