# -*- coding: utf-8 -*-

big = -1
position = 0

for i in range(100):
    number = int(input())
    
    if number > big:
        big = number
        position = i + 1

print(big)
print(position)