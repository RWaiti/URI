# -*- coding: utf-8 -*-

total = 0

X = int(input())
Y = int(input())

if X > Y:
    aux = Y
    Y = X
    X = aux

for i in range(X+1, Y, 1):
    if ((i % 5) == 2) or ((i % 5) == 3):
        print(i)