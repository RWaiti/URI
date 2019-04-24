# -*- coding: utf-8 -*-

from math import trunc

while True:
    thisList = [int(x) for x in input("").split()]
    
    if thisList[0] == 0: 
        break

    A = int(thisList[0])
    B = int(thisList[1])
    C = int(thisList[2])
    
    if A == 0: 
        break
    
    totalHome = A * B
    X = (totalHome*100) / C
    
    print(int(trunc(X**0.5)))