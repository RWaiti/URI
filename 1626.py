# -*- coding: utf-8 -*-

import numpy as np
from math import factorial

def divisores(num):
    n = np.arange(1,num)
    d = num % n
    zeros = d == 0
    aux = 0
    for i in range(len(n)):
        if zeros:
            aux = aux + n[i]
    
# DEF MAIN 

fact = int(input())
fact = factorial(fact)
i = 1
NSumFact = divisores(fact)
    
if NSumFact > 10**9 + 6 and fact > 10**9 + 6:
    NSumFact = NSumFact%(10**9 + 7)
    fact = fact%(10**9 + 7)   
    
elif NSumFact > 10**9 + 6:
    NSumFact = NSumFact%(10**9 + 7)
    
elif fact > 10**9 + 6:
    NSumFact = NSumFact%(10**9 + 7)
    
print (NSumFact, fact)