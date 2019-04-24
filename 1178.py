# -*- coding: utf-8 -*-

array = []
T = float(input())

for i in range(100):
    array.append(T)
    T = T/2

    print('N['+str(i)+'] =', "%.4f" % array[i])