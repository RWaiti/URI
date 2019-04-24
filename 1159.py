# -*- coding: utf-8 -*-

N = int(input())

while N != 0:
    J = 5
    Sum = 0
    
    while J > 0:
        if (N % 2) == 0:
            Sum += N
            J = J - 1 
        N += 1
    
    print(Sum)
    
    N = int(input())