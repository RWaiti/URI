# -*- coding: utf-8 -*-

thisList = [float(0),int(0)]
age = int(input())

while age > 0:
    thisList[1] += 1
    
    thisList[0] += age
    age = int(input())

print("%.2f"%(thisList[0]/thisList[1]))