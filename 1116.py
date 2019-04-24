# -*- coding: utf-8 -*-

N = int(input())


for i in range(N):
    thisList = input().split(' ')
    X = int(thisList[0])
    Y = int(thisList[1])
    
    if Y == 0:
        print('divisao impossivel')
    else:
        print("%.1f"% (X/Y))