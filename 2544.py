# -*- coding: utf-8 -*-

while True:
  try:
    N = int(input())
    i = 0
    while ((N  % 2) == 0 ) and (N != 0):
        N = N/2
        i += 1
    
    print(i)
  except EOFError:
    break