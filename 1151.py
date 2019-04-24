# -*- coding: utf-8 -*-

thisList = [0,1]

for i in range(2,61,1):
  thisList.append(int(thisList[i-1] + thisList[i-2]))

T = int(input())

for i in range(T):
    N = int(input())
    print('Fib(' + str(N) + ') =', thisList[N])