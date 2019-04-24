# -*- coding: utf-8 -*-

result = 0
matrix = []
operator = input()

for i in range(12):
    line = []
    for j in range(12):
        num = float(input())
        line.append(num)
    matrix.append(line)

if operator == 'S':
    for i in range(5):
        for j in range((1 + i), (11 - i)):
            result += matrix[i][j]
            
if operator == 'M':
    for i in range(5):
        for j in range((1 + i), (11 - i)):
            result += matrix[i][j]
    result = result/30
        
print("%.1f" % result)