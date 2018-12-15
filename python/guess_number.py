#!/usr/bin/env python

"""Program losuje liczbę całkowitą z zakresu 1 do 100.
Użytkownik ma 7 prób na zgadnięcie liczby"""

from random import randint

zagadka = randint(1,100)

liczba = 0
proba = 0
maksymalna_proba = 7

print("podaj liczbę 1-100: ")

while(liczba != zagadka):    
    liczba = int(input())
    proba +=1
    #print("Typ liczby: ", type(liczba))
    #print("Typ zagadki: ", type(zagadka))

    if liczba == zagadka:
        print("Zgadłeś za {1} razem!!! Liczba to {0}".format(zagadka, proba))
    else:
        if liczba > zagadka:
            print("Wybierz mniejszą liczbę")
        else:
            print("Wybierz większą liczbę")
    
        if proba >= maksymalna_proba:    
            print("Mogłeś typować tylko {1} razy. Liczba to {0}".format(zagadka, proba))
            break
