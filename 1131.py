# -*- coding: utf-8 -*-

option = 3
contGrenais = 0
contGremio = 0
contInter = 0
contDraw = 0

while option != 2:
    thisList = input().split(' ')
    Inter = int(thisList[0])
    Gremio = int(thisList[1])
    
    option = 3
    contGrenais += 1
    
    if Inter > Gremio:
        contInter += 1
    elif Gremio > Inter:
        contGremio += 1
    else:
        contDraw = 0
    
    while (option != 1) and (option != 2):
        option = int(input('Novo grenal (1-sim 2-nao)\n'))
        
print(str(contGrenais) + ' grenais')
print('Inter:' + str(contInter))
print('Gremio:' + str(contGremio))
print('Empates:' + str(contDraw))

if contInter > contGremio:
    print('Inter venceu mais')
elif contGremio > contInter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')