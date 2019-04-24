# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    print('Ho', end='')
    if i < N-1:
        print(end=' ')
print('!')