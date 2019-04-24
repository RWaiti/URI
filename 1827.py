# -*- coding: utf-8 -*-

while True:
    try:
        matrix = []
        nxm = int(input())

        for i in range(nxm):
            line = []
            for j in range(nxm):
                if int(nxm/3) <= i <= (nxm - int(nxm/3) - 1) and int(nxm/3) <= j <= (nxm - int(nxm/3) - 1):
                    num = 1
                elif i == j:
                    num = 2
                elif (i == nxm - 1 - j) or (j == nxm - 1 - i):
                    num = 3
                else:
                    num = 0
                    
                line.append(num)
            matrix.append(line)
            
        if (nxm%2) != 0:
            matrix[int(nxm/2)][int(nxm/2)] = 4
            
        for i in range(nxm):
            for j in range(nxm):
                print(matrix[i][j], end="")
            print()
        print()
        matrix.clear()
    except EOFError:
        break