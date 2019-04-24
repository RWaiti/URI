# -*- coding: utf-8 -*-

thisList = input().split(' ')
start = int(thisList[0])
finish = int(thisList[1])

if(start > finish) or (start == finish): 
	totalHour = 24-start+finish
elif finish > start: 
	totalHour = finish-start

print('O JOGO DUROU', totalHour , 'HORA(S)')