# -*- coding: utf-8 -*-

N = int(input())
i = 1
thisList = []

while N >= i:
    if (N % i) == 0:
        thisList.append(i)
    i += 1

for i in range (len(thisList)):
    print(thisList[i])