# -*- coding: utf-8 -*-

j = 7

for i in range(1, 10, 2):
    print('I=' + str(i) + ' J=' + str(j))
    print('I=' + str(i) + ' J=' + str(j-1))
    print('I=' + str(i) + ' J=' + str(j-2))
    j += 2