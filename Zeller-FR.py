# -*- coding: utf-8 -*-
######################################## {{{{{{{{{{{{{{{{Congruence de zeller}}}}}}}}}}}}}}}} ######################################
from math import *
def zeller():
    jourSemaine={0:'samedi',
                1:'dimanche',
                2:'lundi',
                3:'mardi',
                4:'mercredi',
                5:'jeudi',
                6:'vendredi'}
    
    print("Entrez une date sous le format \n jour(1-31)/mois(1-12)/annee")
    
    q, mois, annee = [int(x) for x in input("Enter the date: ").split('/')]
    if mois >= 3:
        m = mois
    else :
        m=mois+12
        annee -= 1
    
    j=annee // 100
    k=annee%100

    #Calcul du jour de la semaine
    h=(q+floor(26*(m+1)/10)+k+floor(k/4)+floor(j/4)+5*j)%7

    print("Cette date correspond à un " + jourSemaine[h])

zeller()
