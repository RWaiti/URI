# -*- coding: utf-8 -*-

lista = input().split(' ')
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])
D = int(lista[3])

if ((B>C) and (D>A) and ((C+D)>(A+B)) and (C>0) and (D>0) and ((A%2)==0)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')