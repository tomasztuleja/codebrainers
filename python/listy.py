#!/usr/bin/env python

#wypelnienie list:

lista1 = [x**2 for x in range(1,100000)]
lista2 = [x**3 for x in range(1,50000)] 

#print(lista1, lista2)

#print("dlugosc listy pierwszej to {}, a drugiej to {}".format(len(lista1), len(lista2)))


#zadeklarowanie list
wspolna = []
pierwiastki = []

#wypisywanie wspolnych elementow obu list:

#for el in lista1:
 #   if el in lista2:
  #      wspolna.append(el)
   # else:
    #    continue

#rzutowanie list na sety:

set1 = set(lista1)
set2 = set(lista2)
set3 = set1 & set2

#rzutowanie setu na liste:

list3 = list(set3)

#pierwiastkowanie kazdego elementu list3:

for p in list3:
    pierwiastki.append((p**0.5))


            


#print(set3)
#print(len(set3))

print(list3)

print(pierwiastki)
print(len(pierwiastki))


