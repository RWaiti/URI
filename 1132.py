# -*- coding: utf-8 -*-

total = 0

X = int(input())
Y = int(input())

if X > Y:
    aux = Y
    Y = X
    X = aux

for i in range(X, Y+1, 1):
    if ((i % 13) != 0):
        total = total + i

print(total)