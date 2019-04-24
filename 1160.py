# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    thisList = input().split(' ')
    PA = int(thisList[0])
    PB = int(thisList[1])
    G1 = float(thisList[2])
    G2 = float(thisList[3])

    i = 0
    
    while (PA <= PB) and (i != 101):
        PA = PA + int(PA*G1*0.01)
        i += 1
        if G2>0:
            PB = PB + int(PB*G2*0.01)
    
    if i > 100:
        print('Mais de 1 seculo.')
    else:
        print(i, 'anos.')