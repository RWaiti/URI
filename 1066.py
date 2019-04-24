# -*- coding: utf-8 -*-

contPar = 0 
contImpar = 0 
contPos = 0 
contNeg = 0 

for i in range(5):
    number = int(input())
    
    if (number%2) == 0:
        contPar += 1
        
    else:
        contImpar += 1
        
    if number > 0:
        contPos += 1
        
    elif number < 0:
        contNeg += 1

print(contPar, 'valor(es) par(es)')
print(contImpar, 'valor(es) impar(es)')
print(contPos, 'valor(es) positivo(s)')
print(contNeg, 'valor(es) negativo(s)')