# -*- coding: utf-8 -*-

amount = int(input())
numIn = 0
numOut = 0

for i in range(amount):
    X = int(input())
    if (X >= 10) and (X <= 20):
        numIn += 1
    else:
        numOut += 1

print(numIn,'in')
print(numOut,'out')