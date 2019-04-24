# -*- coding: utf-8 -*-

thisList = input().split(' ')
startHour = int(thisList[0])
startMin = int(thisList[1])
finishHour = int(thisList[2])
finishMin = int(thisList[3])


if (startHour > finishHour):
    totalHour = 24 - startHour + finishHour
    if startMin > finishMin:
        totalMin = 60 - startMin + finishMin
        totalHour -= 1
        if(totalMin>= 60):
            totalHour += 1
            totalMin -= 60
    else:
        totalMin = startMin + finishMin
        
elif (startHour == finishHour) and (startMin == finishMin):
    totalHour = 24
    totalMin = 0    
    
elif (startHour == finishHour) and (startMin != finishMin):
    totalHour = 0
    if startMin > finishMin:
        totalMin = 60 - startMin + finishMin
        totalHour -= 1
        if(totalMin>= 60):
            totalHour += 1
            totalMin -= 60
    else:
        totalMin = finishMin - startMin
        
elif finishHour > startHour:
    totalHour = finishHour - startHour
    if startMin > finishMin:
        totalMin = 60 - startMin + finishMin
        totalHour -= 1
        if(totalMin>= 60):
            totalHour += 1
            totalMin -= 60
    else:
        totalMin = finishMin - startMin

print('O JOGO DUROU', totalHour , 'HORA(S) E', totalMin, 'MINUTOS(S)')