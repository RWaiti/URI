# -*- coding: utf-8 -*-

cont = 0 
media = 0

for i in range(6):
    number = float(input())
    
    if number > 0:
        media = media + number
        cont += 1

print(aux,'valores positivos')
print("%.1f"%(media/cont))