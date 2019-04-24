# -*- coding: utf-8 -*-

evenList = []
oddList = []
even = 0
odd = 0

for i in range(15):
    N = int(input())
    
    if (N % 2) == 0:
        evenList.append(N)
        even += 1
    else:
        oddList.append(N)
        odd += 1
    
    if odd == 5:
        for i in range(len(oddList)):
            print('impar[' + str(i) + '] =', oddList[i])
        oddList.clear()
        odd = 0
        
    if even == 5:
        for i in range(len(evenList)):
            print('par[' + str(i) + '] =', evenList[i])
        evenList.clear()
        even = 0

for i in range(len(oddList)):
    print('impar[' + str(i) + '] =', oddList[i])

for i in range(len(evenList)):
    print('par[' + str(i) + '] =', evenList[i])


        