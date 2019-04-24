# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    thisList = input().split(' ')
    X = int(thisList[0])
    Y = int(thisList[1])
    
    J = Y
    Sum = 0
    
    while J > 0:
        if (X % 2) != 0:
            Sum += X
            J = J - 1 
        X += 1
    
    print(Sum)