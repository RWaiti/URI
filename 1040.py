# -*- coding: utf-8 -*-

lista = input().split(' ')
N1 = float(lista[0])
N2 = float(lista[1])
N3 = float(lista[2])
N4 = float(lista[3])

grade = (N1*2 + N2*3 + N3*4 + N4*1) / 10

print('Media:',"%.1f" % grade)

if grade>=7:
    print('Aluno aprovado.')
elif grade < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exameN = float(input())
    print('Nota do exame:',"%.1f" %  exameN)
    grade = (exameN + grade)/2
    
    if grade >=5:
            print('Aluno aprovado.')
    else:
            print('Aluno reprovado.')
            
    print('Media final:',"%.1f" % grade)