# -*- coding: utf-8 -*-

class stack(object):
    def __init__(self):
        self.data = []
        
    def empty(self):
        return len(self.data) == 0
 
    def push(self, elemento):
        self.data.append(elemento)
 
    def pop(self):
        if not self.empty():
            return self.data.pop(-1)


N = int(input())
P = stack()
auxP = stack()
big = 0

for i in range(N):
    thisList = input().split(' ')
    print(thisList[0], '<=--')
    
    if thisList[0] == 'PUSH':
        print(thisList[1])
        P.push(int(thisList[1]))
        
    elif thisList[0] == 'MIN':
        if not P.empty:
            while not P.empty:
                aux = P.pop()
                auxP.pop(aux)
                if aux > big:
                   big = aux
                   
            while not auxP.empty:
                P.push(auxP.pop())    
            
            print(big)
    elif thisList[0] == 'POP':
        print P.pop