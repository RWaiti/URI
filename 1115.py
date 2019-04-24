# -*- coding: utf-8 -*-

x = 1
y = 2

while (x != 0) and (y != 0):
    lista = input().split(' ')
    x = int(lista[0])
    y = int(lista[1])
    
    if (x != 0) and (y != 0):
        if x > 0:
            if y > 0:
                print('primeiro')
            else:
                print('quarto')
        else:
            if y > 0:
                print('segundo')
            else:
                print('terceiro')