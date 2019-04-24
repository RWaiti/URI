# -*- coding: utf-8 -*-

cont = 0 

for i in range(5):
    number = int(input())
    
    if (number%2) == 0:
        cont += 1

print(cont,'valores pares')