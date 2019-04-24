# -*- coding: utf-8 -*-

N = int(input())

for j in range(N):
    thisList = input().split(' ')
    X = int(thisList[0])
    Y = int(thisList[1])
    
    total = 0
    i = 0
    
    if X > Y:
        aux = Y
        Y = X
        X = aux
    
    for i in range(X+1,Y):
        if ((i % 2) != 0):
            total = total + i
            
    print(total)