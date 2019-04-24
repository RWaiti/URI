# -*- coding: utf-8 -*-

priceList = [4, 4.50, 5, 2, 1.50]

thislist = input().split(' ')
code = int(thislist[0])
quantity = int(thislist[1])

total = priceList[code - 1] * quantity

print('Total: R$', "%.2f" % total)