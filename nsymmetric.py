# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:32:54 2022

@author: asus
"""

import numpy as np
import math
import re
import galois
from dmin import*
###############################################################################
def nsymmetric(d, n):
    [h, g]= dmin(d, n)
    a=len(h)
    H=[]
    GF = galois.GF(2**n)
    b = GF.primitive_element
    for i in range (a):
        c=h[i]
        d=c[0]
        e=b**d
        f=e.minimal_poly()
        l=f.coeffs
        m=l.tolist()
        H.append(m)
    GF = galois.GF(2)
    o = galois.Poly([1], field=GF)
    for j in range (len(H)):
        p=H[j]
        q = galois.Poly( p , field=GF)
        o = o*q
    r = 2**((2**n)-1)+1
    s=[int(i) for i in bin(r)[2:]]
    t= galois.Poly( s , field=GF)
    U = t // o
    V=U.coeffs
    u=V.tolist()
    v=[item for sublist in h for item in sublist]
    w=len(v)
    x=2**w
    return(x, u)
    
    
    
        
    
    