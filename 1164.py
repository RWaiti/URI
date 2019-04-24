# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    X = int(input())
    i = 1
    thisList = []
    aux = 0
    
    while X >= i:
        if (X % i) == 0:
            aux += 1
        i += 1
    
    if aux == 2:
        print(X,'eh primo')
    else:
        print(X,'nao eh primo')