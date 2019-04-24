# -*- coding: utf-8 -*-

lista = input().split(' ')
N1 = int(lista[0])
N2 = int(lista[1])
N3 = int(lista[2])

if N1 > N2:
    auxN = N1
    N1 = N2
    N2 = auxN
    
if N2 > N3:
    auxN = N2
    N2 = N3
    N3 = auxN
    
if N1 > N2:
    auxN = N1
    N1 = N2
    N2 = auxN
    
print(N1)
print(N2)
print(N3)
print()
print(int(lista[0]))
print(int(lista[1]))
print(int(lista[2]))