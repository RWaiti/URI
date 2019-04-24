# -*- coding: utf-8 -*-
X = 1
Y = 2

while (X != Y):
    thisList = input().split(' ')
    X = int(thisList[0])
    Y = int(thisList[1])
    
    if (X != Y):
        if X > Y:
            print('Decrescente')
        else:
            print('Crescente')