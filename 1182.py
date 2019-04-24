# -*- coding: utf-8 -*-

result = 0
matrix = []

whoLine = int(input())
operator = input()

for i in range(12):
    line = []
    for j in range(12):
        num = float(input())
        line.append(num)
    matrix.append(line)

if operator == 'S':
    for i in range(12):
        result += matrix[i][whoLine]
            
if operator == 'M':
    for i in range(12):
        result += matrix[i][whoLine]
    result = result/12
        
print("%.1f" % result)