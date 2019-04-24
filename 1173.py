# -*- coding: utf-8 -*-

array = []

N = int(input())
array.append(N)

for i in range(9):
    N *= 2
    array.append(N)

for i in range(10):    
    print('N['+str(i)+'] =',array[i])