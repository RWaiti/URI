# -*- coding: utf-8 -*-

N = int(input())
small = 99999999
array = input().split(' ')
    
for i in range(N):
    if int(array [i]) < small:
        small = int(array [i])
        position = i

print('Menor valor:', small)
print('Posicao:', position)