# -*- coding: utf-8 -*-

N = int(input())
stars = input().split(' ')
total = 0
j = 0

for i in range(N):
    if (int(stars[i])%2) != 0:
        