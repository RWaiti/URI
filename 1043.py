# -*- coding: utf-8 -*-

import math

lista = input().split(' ')
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

itsATriangle = 0

if math.fabs(B - C) < A < B + C:
    itsATriangle += 1
if math.fabs(A - C) < B < A + C:
    itsATriangle += 1
if math.fabs(A - B) < C < A + B:
    itsATriangle += 1

if itsATriangle == 3:
    result = A + B + C
    print('Perimetro =', "%.1f" % result)
else:
    result = ((A+B)*C)/2
    print('Area =',"%.1f" % result)