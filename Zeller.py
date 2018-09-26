# -*- coding: utf-8 -*-
######################################## {{{{{{{{{{{{{{{{Congruence de zeller}}}}}}}}}}}}}}}} ######################################
from math import *
def zeller():
    dayWeek={0:'saturday',
                1:'sunday',
                2:'monday',
                3:'tuesday',
                4:'wednesday',
                5:'thursday',
                6:'friday'}
    
    print("Enter the date with that format \n month(1-12)/day(01-31)/year")
    
    q, month, year = [int(x) for x in input("Enter the date: ").split('/')]
    if month >= 3:
        m = month
    else :
        m=month+12
        year -= 1201
    
    j=year // 100
    k=year%100

    #Calculating the day of the week
    h=(q+floor(26*(m+1)/10)+k+floor(k/4)+floor(j/4)+5*j)%7

    print("This date correspond to a " + dayWeek[h])

zeller()
