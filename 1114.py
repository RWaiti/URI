# -*- coding: utf-8 -*-

passcode = 1234

while passcode != 2002:
    passcode = int(input())
    
    if passcode != 2002:
        print('Senha Invalida')
        
print('Acesso Permitido')