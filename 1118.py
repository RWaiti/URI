# -*- coding: utf-8 -*-

option = 3

while option != 2:
    aux = 0
    grade = 0
    option = 3
    
    while aux !=2:
        number = float(input())
        
        if 0 <= number <= 10:
            grade = grade + number
            aux += 1
        else:
            print('nota invalida')
    
    print('media =',"%.2f"% (grade/2))
    
    while (option != 1) and (option != 2):
        option = int(input('novo calculo (1-sim 2-nao)\n'))