# -*- coding: utf-8 -*-

N = 1

while N != 0:
    N = int(input())
    if N != 0:
        for i in range(N):
            print (str(i+1),end="")
            if i+1 != N:
                print(' ',end="")
        
        print()