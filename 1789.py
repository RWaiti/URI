# -*- coding: utf-8 -*-

while True:
  try:
    aux = 0
    L = int(input())
    thisList = input().split(' ')
    for i in range(L):
        if int(thisList[i]) > aux:
            aux = int (thisList[i])
    if 10 <= aux < 20:
        print(2)
    elif aux >= 20:
        print(3)
    else:
        print(1)
    thisList.clear()
  except EOFError:
    break