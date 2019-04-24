# -*- coding: utf-8 -*-

matrix = []

while True:
    nxm = int(input())
    width = len(str((2 ** (nxm-1)) ** 2))
    
    if not nxm:
        break
    
    for i in range(nxm):
        line = []
        for j in range(nxm):
            if j == 0 and i == 0:
                num = 1 
            elif i == 0:
                num = line[i-1] * 2
            else:
                num = matrix[i-1][j] * 2
            line.append(num)
        matrix.append(line)
    
    for i in range(nxm):
        for j in range(nxm):
            print('{:{}d}'.format(matrix[i][j], width), end = '')
            
            if j != (nxm-1):
                print(end=" ")
                
        print()
    print()
    
    matrix.clear()