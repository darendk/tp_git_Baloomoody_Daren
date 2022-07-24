#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
        return a+b

#ce program va tester si le nombre d'argument est correct.
nombre_argument=len(sys.argv)-1
if (nombre_argument < 2):
        print("Vous n'avez pas inserrer les 2 valeurs en argument")
        x=int(input("Inserrez la première valeur: "))
        y=int(input("Inserrez la deuxième valeur: "))
elif (nombre_argument > 2):
        print("Mettez uniquement les 2 valeurs à ajouter en argument")
else :
        x=int(sys.argv[1])
        y=int(sys.argv[2])

print(add(x,y))


