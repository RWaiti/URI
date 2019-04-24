# -*- coding: utf-8 -*-

gasList = [0, 0, 0]
X = 0

while X != 4:
    X = 0
    
    X = int(input())
    
    if X == 1:
        gasList[0] += 1
    elif X == 2:
        gasList[1] += 1
    elif X == 3:
        gasList[2] += 1

print('MUITO OBRIGADO')
print('Alcool:', gasList[0])
print('Gasolina:', gasList[1])
print('Diesel:', gasList[2])