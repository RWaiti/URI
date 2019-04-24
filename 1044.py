# -*- coding: utf-8 -*-

lista = input().split(' ')
A = int(lista[0])
B = int(lista[1])

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')