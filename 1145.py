# -*- coding: utf-8 -*-

cont = 0

thisList = input().split(' ')
X = int(thisList[0])
Y = int(thisList[1])

for i in range(Y):
    cont += 1
    
    print (str(i+1), end="")
    
    if cont == X:
        print()
        cont = 0
    else:
        print(' ',end="")