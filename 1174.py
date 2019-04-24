# -*- coding: utf-8 -*-

array = []

for i in range(100):
    A = float(input())
    array.append(A)

for i in range(100):
    if array[i] <= 10:
        print('A['+str(i)+'] =',"%.1f"%array[i])