#!/usr/bin/env python
from random import randint

#lista 6 losowych z 49

wynik = []
for i in range(1, 7):
    wynik.append(randint(1,49))

losy = []
traf = []

#liczby gracza przez petle for



print("""
Wprowadź 6 liczb całkowitych od 1 - 49.

Po każdej liczbie naciśnij ENTER:
""")


# Wprowadzam kolejno 6 liczb


for i in range(1,7):    
    losy.append(int(input())) 

                 


# Porównje każdą liczbę z listy wynik z każdą liczbą z isty losy, jeśli wspólne, tworze liste traf
for i in wynik:
    for j in losy:
        if j == i:
            traf.append(j)
        else:
            continue
print("""Wynik losowania:
""", wynik)

print("""Twoje liczby to:
""", losy)

print("Trafiłeś ",(len(traf))," liczb")

if len(traf) != 0:
    print("""Trafione lizby to: 
    """, traf)
