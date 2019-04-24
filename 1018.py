# -*- coding: utf-8 -*-

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0


A = int(input())
B = A

if (A >= 100):
    nota100 = int(A/100)
    A = A - 100*nota100
    
if (A >= 50):
    nota50 = int(A/50)
    A = A - 50*nota50
    
if (A >= 20):
    nota20 = int(A/20)
    A = A - 20*nota20
    
if (A >= 10):
    nota10 = int(A/10)
    A = A - 10*nota10
    
if (A >= 5):
    nota5 = int(A/5)
    A = A - 5*nota5
    
if (A >= 2):
    nota2 = int(A/2)
    A = A - 2*nota2
    
if (A >= 1):
    nota1 = int(A/1)
    A = A - 1*nota1
    
print(B)
print(nota100, 'nota(s) de R$ 100,00')
print(nota50, 'nota(s) de R$ 50,00')
print(nota20, 'nota(s) de R$ 20,00')
print(nota10, 'nota(s) de R$ 10,00')
print(nota5, 'nota(s) de R$ 5,00')
print(nota2, 'nota(s) de R$ 2,00')
print(nota1, 'nota(s) de R$ 1,00')