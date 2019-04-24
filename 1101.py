# -*- coding: utf-8 -*-

M = 1
N = 1

while (M > 0) and (N > 0):
    thisList = input().split(' ')
    M = int(thisList[0])
    N = int(thisList[1])
    
    if (M > 0) and (N > 0):
        if M > N:
            aux = N
            N = M
            M = aux
        
        aux = 0
        
        for i in range(M, N+1, 1):
            print(i, end=" ")
            aux = aux + i
        
        print('Sum=' + str(aux))