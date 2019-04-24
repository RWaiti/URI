# -*- coding: utf-8 -*-

matrix = []


while True:
  try:
    nxm = int(input())
    
    for i in range(nxm):
        line = []
        for j in range(nxm):
            if (i + j) == nxm-1:
                num = 2
            elif i == j:
                num = 1
            else:
                num = 3
            line.append(num)
        matrix.append(line)
    
    for i in range(nxm):
        for j in range(nxm):
            print(matrix[i][j], end="")
        if i < nxm-1:
            print()
        
    matrix.clear()
    print()
  except EOFError:
    break