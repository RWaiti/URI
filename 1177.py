# -*- coding: utf-8 -*-

array = []
T = int(input())
aux = 0

for i in range(1000):
    array.append(aux)
    
    if aux == T-1:
        aux = 0
    else:
        aux += 1
    
    print('N['+str(i)+'] =', array[i])