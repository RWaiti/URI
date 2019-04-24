# -*- coding: utf-8 -*-

years = 0
months = 0

days = int(input())

if (days >= 365 ):
    years = int(days/365 )
    days = days - 365 *years
    1
if (days >= 30):
    months = int(days/30)
    days = days - 30*months
    
    print(years ,'ano(s)')
    print(months ,'mes(es)')
    print(days ,'dia(s)')