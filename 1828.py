# -*- coding: utf-8 -*-

T = int(input())

for i in range(1,T+1):
    thisList = input().split(' ')
    Sheldon = thisList[0]
    Raj = thisList[1]
    
    
    if Sheldon == Raj:
        print('Caso #' + str(i) + ': De novo!')
    
    elif Sheldon == 'pedra':
        if Raj == 'lagarto' or Raj == 'tesoura':
            print('Caso #' + str(i) + ': Bazinga!')
                  
        elif Raj == 'papel' or Raj == 'Spock':
            print('Caso #' + str(i) + ': Raj trapaceou!')
                  
    elif Sheldon == 'papel':
        if Raj == 'pedra' or Raj == 'Spock':
            print('Caso #' + str(i) + ': Bazinga!')
                  
        elif Raj == 'lagarto' or Raj == 'tesoura':
            print('Caso #' + str(i) + ': Raj trapaceou!')
                  
    elif Sheldon == 'tesoura':
        if Raj == 'papel' or Raj == 'lagarto':
            print('Caso #' + str(i) + ': Bazinga!')
                  
        elif Raj == 'pedra' or Raj == 'Spock':
            print('Caso #' + str(i) + ': Raj trapaceou!')
                  
    elif Sheldon == 'lagarto':
        if Raj == 'Spock' or Raj == 'papel':
            print('Caso #' + str(i) + ': Bazinga!')
                  
        elif Raj == 'tesoura' or Raj == 'pedra':
            print('Caso #' + str(i) + ': Raj trapaceou!')
                  
    elif Sheldon == 'Spock':
        if Raj == 'tesoura' or Raj == 'pedra':
            print('Caso #' + str(i) + ': Bazinga!')
                  
        elif Raj == 'papel' or Raj == 'lagarto':
            print('Caso #' + str(i) + ': Raj trapaceou!')