# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:32:55 2023

@author: asus
"""

import math
from custom import*
from custom2 import*
####################################################################################
def bipolar( k , n):
    a = math.log(k, 2)
    b = math.ceil(a)
    m = 2*(b+1)
    if n <= ( 2**(m-1) + 2**((m/2)-1) )* ( 2**(m/2) - 1):
        d = int(2**(m - 1) - 2**((m/2) - 1) - 1)
        A = custom(d, m, n)
    else:
        m = m+1
        if n <= (2**(m) - 2**(m - 1) + 1)*(2**(m)-1):
            d = int(2**(m-1) - 2**((m-1)/2)-1)
            A = custom2(d, m , n )
        else:
            m = m+1
            if n <= (2**(m/2) - 1)*(2**(2*m - 1) + 2**(((3*m)/2)-2) - 2**(m-2)+2**(m/2)+1):
                d = int(2**(m-1) - 2**(m/2)-1)
                A = custom2(d , m , n)
            else:
                m = m+1
                if n <= (2**(m)-1)*(9*(2**(2*m-4))+3*(2**(m-3))+1):
                    d = int(2**(m-1)-2**((m+1)/2)-1)
                    A = custom2(d, m, n)
                else:
                    print("Value of n is too large")
    return(A)
                
        
    