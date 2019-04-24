# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    thisList = list(input())
    lengthList = len(thisList)
    
    for j in range(lengthList-1,-1,-1):
        if ('A' <= thisList[j] <= 'Z') or ('a' <= thisList[j] <= 'z'):
            thisList[j] = chr(ord(thisList[j])+3)
        if (lengthList)/2 > j:
            thisList[j] = chr(ord(thisList[j])-1)
        print(thisList[j],end = '')
    print()