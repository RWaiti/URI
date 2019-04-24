# -*- coding: utf-8 -*-

N = int(input())
total = 0
totalC = 0
totalR = 0
totalS = 0

for i in range(N):
    thisList = input().split(' ')
    amount = int(thisList[0])
    Type = thisList[1]
    
    total += amount
    
    if Type == 'C':
        totalC += amount
    if Type == 'R':
        totalR += amount
    if Type == 'S':
        totalS += amount

print('Total:', total, 'cobaias')
print('Total de coelhos:',totalC)
print('Total de ratos:',totalR)
print('Total de sapos:',totalS)
print('Percentual de coelhos:', "%.2f"% (100*totalC/total),'%')
print('Percentual de ratos:', "%.2f"% (100*totalR/total),'%')
print('Percentual de sapos:', "%.2f"% (100*totalS/total),'%')