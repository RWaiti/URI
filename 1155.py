# -*- coding: utf-8 -*-

S = 0
aux = 0

for i in range(1, 40, 2):
    S = S + (i / 2**aux)
    aux += 1
    
print("%.2f"%S)