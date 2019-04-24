# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    lista = input().split(' ')
    A = float(lista[0])
    B = float(lista[1])
    C = float(lista[2])
    
    media = ((A * 2) + (B * 3) + (C * 5)) / 10
    
    print("%.1f"%media)