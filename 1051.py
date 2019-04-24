# -*- coding: utf-8 -*-

salary = float(input())
salary -= 2000

if salary < 0:
    print('Isento')
    
else:
    if salary > 1000:
        auxSalary = 1000 * 0.08
    else:
        auxSalary = salary * 0.08
        
    salary -= 1000
    if salary < 0 :
        print('R$', "%.2f"%auxSalary)
    else:
        if salary > 1500:
            auxSalary = 1500 * 0.18 + auxSalary
        else:
            auxSalary = salary * 0.18 + auxSalary
        
        salary -= 1500
        if salary < 0 :
            print('R$', "%.2f"%auxSalary)
        else:
            auxSalary = salary * 0.28 + auxSalary
            print('R$', "%.2f"%auxSalary)