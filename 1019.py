# -*- coding: utf-8 -*-

hours = 0
minutes = 0

N = int(input())

if (N >= 3600):
    hours = int(N/3600)
    N = N - 3600*hours
    1
if (N >= 60):
    minutes = int(N/60)
    N = N - 60*minutes
    
print(str(hours) + ':' + str(minutes) + ':' + str(N))