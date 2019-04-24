# -*- coding: utf-8 -*-

aux = 0
grade = 0

while aux !=2:
    number = float(input())
    
    if 0 <= number <= 10:
        grade = grade + number
        aux += 1
    else:
        print('nota invalida')

print('media =',grade/2)