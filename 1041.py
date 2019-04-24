# -*- coding: utf-8 -*-

lista = input().split(' ')
x = float(lista[0])
y = float(lista[1])

if  x == y == 0:
    print('Origem')
elif x == 0 or y == 0:
    if  x == 0:
        print('Eixo Y')
    else:
        print('Eixo X')
elif x > 0:
    if y > 0:
        print('Q1')
    else:
        print('Q4')
else:
    if y > 0:
        print('Q2')
    else:
        print('Q3')