# -*- coding: utf-8 -*-

N = int(input())

for i in range(1,10001,1):
    if(round(i%N,1) == 2):
        print(i)