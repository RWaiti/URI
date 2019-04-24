# -*- coding: utf-8 -*-

thisList1= input().split(' ')
day = thisList1[0]
StartDay = int(thisList1[1]) 

thisList2= input().split(' : ')
startHour = int(thisList2[0])
startMin = int(thisList2[1])
startSec = int(thisList2[2])

thisList1= input().split(' ')
day = thisList1[0]
finishDay = int(thisList1[1]) 

thisList2= input().split(' : ')
finishHour = int(thisList2[0])
finishMin = int(thisList2[1])
finishSec = int(thisList2[2])


totalDay = finishDay - StartDay

if startHour > finishHour: 
    totalDay = totalDay - 1 
    totalHour = (24 - startHour) + finishHour

elif startHour <= finishHour: 
    totalHour = finishHour - startHour

if startMin > finishMin: 
    totalHour = totalHour - 1 
    totalMin = (60 - startMin) + finishMin

elif startMin <= finishMin: 
    totalMin = finishMin - startMin

if startSec > finishSec: 
    totalMin = totalMin - 1 
    totalSec = (60 - startSec) + finishSec

elif startSec <= finishSec: 
    totalSec = finishSec - startSec

if totalSec > 60: 
    totalSec -= 60
    totalMin += 1

if totalMin > 60: 
    totalMin -= 60
    totalHour += 1
    
if totalHour > 24: 
    totalHour -= 24
    totalDay += 1

print(totalDay, "dia(s)") 
print(totalHour, "hora(s)") 
print(totalMin, "minuto(s)") 
print(totalSec, "segundo(s)")