# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())
total = 0
i = 0

if X > Y:
    aux = Y
    Y = X
    X = aux

for i in range(X+1,Y):
    if ((i % 2) != 0):
        total = total + i

print(total)