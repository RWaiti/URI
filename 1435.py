# -*- coding: utf-8 -*-

while True:
    nxm = int(input())
    
    if nxm == 0:
        break
    
    for i in range(1, nxm+1):
        for j in range(1, nxm+1):
            aux = i
            if(j < aux):
                aux = j
            if(nxm-j+1 < aux):
                aux = nxm-j+1
            if(nxm-i+1 < aux):
                aux = nxm-i+1
            print("%3d"%aux, end = '');
            if j != (nxm):
                print(end=" ")
        print()
    print()