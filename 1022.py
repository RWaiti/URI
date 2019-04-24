# -*- coding: utf-8 -*-

N = int(input())


for i in range(N):
    thisList = input().split(' ')
    N1 = int(thisList[0])
    D1 = int(thisList[2])
    symbol = thisList[3]
    N2 = int(thisList[4])
    D2 = int(thisList[6])

    thisList.clear()
    
    if symbol == '+':
        N3 = (N1*D2 + N2*D1)
        D3 = (D1*D2)
    elif symbol == '-':
        N3 = (N1*D2 - N2*D1)
        D3 = (D1*D2)
    elif symbol == '*':
        N3 = (N1*N2)
        D3 = (D1*D2)
    elif symbol == '/':
        N3 = (N1*D2)
        D3 = (N2*D1)
 
    N4 = N3       
    D4 = D3
    flag = 1
    
    while flag:
        flag = 0
        if (N4%2) == 0 and (D4%2) == 0 and D4 != 0 and N4 != 0:
            N4 = int(N4 / 2)
            D4 = int(D4 / 2)
            flag = 1
        elif (N4%3) == 0 and (D4%3) == 0 and D4 != 0 and N4 != 0:
            N4 = int(N4 / 3)
            D4 = int(D4 / 3)
            flag = 1
        elif (N4%5) == 0 and (D4%5) == 0 and D4 != 0 and N4 != 0:
            N4 = int(N4 / 5)
            D4 = int(D4 / 5)
            flag = 1
    
    print(str(N3) + '/' + str(D3) + ' = ' + str(N4) + '/' + str(D4))