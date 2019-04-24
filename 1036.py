# -*- coding: utf-8 -*-

from math import sqrt

lista = input().split(' ')
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

delta = float((B**2) - (4*A*C))

if (delta < 0) or (A == 0):
    print('Impossivel calcular')
else:
    sqrtt = float(sqrt(delta))
    bhaskP = (-B + sqrtt)/ (2*A)
    bhaskN = (-B - sqrtt)/ (2*A)

    print('R1 =',"%.5f" % bhaskP)
    print('R2 =',"%.5f" % bhaskN)