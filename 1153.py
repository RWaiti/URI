# -*- coding: utf-8 -*-

def fat(N):
    if (N == 1) or (N == 0):
        return 1
    else:
        return fat(N-1) * N

N = int(input())

num = fat(N)

print(num)