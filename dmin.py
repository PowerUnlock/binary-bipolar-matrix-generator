# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:11:20 2022

@author: asus
"""

import numpy as np
import math
from cyclo import*
import itertools
##################################################################################
def dmin(d, n):
    D=cyclo(n)
    G=[]
    for i in range(1,d):
        for j in range(len(D)):
            if i in D[j]:
                G.append(D[j])
                break
            else:
                 continue
    G.sort()
    z=list(G for G,_ in itertools.groupby(G))
    a={tuple(x) for x in D}
    b={tuple(x) for x in z}
    u=a.difference(b)
    h=[list(tup) for tup in u]
    v=[item for sublist in z for item in sublist]
    g=sorted(v)
    return(h, g)
    
    