# -*- coding: utf-8 -*-

array = []

for i in range(20):
    Y = int(input())
    array.append(Y)
    
for i in range(10):
    aux = array[i]
    array[i] = array[19 - i]
    array[19 - i] = aux

for i in range(20):
        print('N['+str(i)+'] =', array[i])