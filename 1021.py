# -*- coding: utf-8 -*-

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda05 = 0
moeda01 = 0

thisList = input().split('.')
integer = int(thisList[0])
decimal = int(thisList[1])

if (integer >= 100):
    nota100 = int(integer/100)
    integer = integer - 100*nota100
    
if (integer >= 50):
    nota50 = int(integer/50)
    integer = integer - 50*nota50
    
if (integer >= 20):
    nota20 = int(integer/20)
    integer = integer - 20.0*nota20
    
if (integer >= 10):
    nota10 = int(integer/10)
    integer = integer - 10*nota10
    
if (integer >= 5):
    nota5 = int(integer/5)
    integer = integer - 5*nota5
    
if (integer >= 2):
    nota2 = int(integer/2)
    integer = integer - 2*nota2
    
if (integer >= 1):
    moeda1 = int(integer/1)
    integer = integer - 1*moeda1
    
if (decimal >= 50):
    moeda50 = int(decimal/50)
    decimal = decimal - 50*moeda50

if (decimal >= 25):
    moeda25 = 1
    decimal = decimal - 25

if (decimal >= 10):
    moeda10 = int(decimal/10)
    decimal = decimal - 10*moeda10

if (decimal >= 5):
    moeda05 = 1
    decimal = decimal - 5
    
if (decimal >= 1):
    moeda01 = int(decimal/1)
    decimal = decimal - 1*moeda01

print('NOTAS:') 
print(nota100, 'nota(s) de R$ 100.00')
print(nota50, 'nota(s) de R$ 50.00')
print(nota20, 'nota(s) de R$ 20.00')
print(nota10, 'nota(s) de R$ 10.00')
print(nota5, 'nota(s) de R$ 5.00')
print(nota2, 'nota(s) de R$ 2.00')
print('MOEDAS:') 
print(moeda1, 'moeda(s) de R$ 1.00')
print(moeda50, 'moeda(s) de R$ 0.50')
print(moeda25, 'moeda(s) de R$ 0.25')
print(moeda10, 'moeda(s) de R$ 0.10')
print(moeda05, 'moeda(s) de R$ 0.05')
print(moeda01, 'moeda(s) de R$ 0.01')