# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:42:06 2022

@author: asus
"""

import numpy as np
import math
############################################################################################
def cyclo(n):
    a=2**n-1
    b=list(range(1,a))
    c=[]
    while (len(b)>0):
        d=sorted(b)
        e=d[0]
        f=[]
        f.append(e)
        for j in range (1,a):
            g=((2**j)*e)% a
            if g== e:
                c.append(f)
                b= list(set(b) - set(f))
                break
            else:
                f.append(g)
    return (c)    
            
                
