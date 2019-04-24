# -*- coding: utf-8 -*-

nxm = int(input())

while nxm > 0:
    for i in range(1,nxm+1):
        aux = i
        aux2 = 2
        
        for j in range(i):
            print("%3d"%aux, end="")
            if j != (nxm-1):
                print(end=" ")
            aux -= 1
            
        for j in range(i,nxm):
            print("%3d"%aux2, end="")
            if j != (nxm-1):
                print(end=" ")
            aux2 += 1
        print()
    print()
    nxm = int(input())