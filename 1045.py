# -*- coding: utf-8 -*-

lista = input().split(' ')
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])


while (A < B) or (B < C) or (A < C):
    if A < B:
        auxN = A
        A = B
        B = auxN
        
    if B < C:
        auxN = B
        B = C
        C = auxN

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:  
    if A*A  == (B*B + C*C):
        print('TRIANGULO RETANGULO')
    if A*A  > (B*B + C*C):
        print('TRIANGULO OBTUSANGULO')
    if A*A < (B*B + C*C):
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif (A == B and A != C and B != C) or (B == C and B != A and C != A) or (A == C and A != B and C != B) :
        print('TRIANGULO ISOSCELES')  