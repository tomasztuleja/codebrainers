#!/usr/bin/env python

#imiona = ["Hamlet", "Macbeth", "Ophelia", "Henrey"]

#for imie in imiona:
#    print("Imie: {}".format(imie))


sonet42 = """That thou hast her it is not all my grief,
And yet it may be said I loved her dearly,
That she hath thee is of my wailing chief,
A loss in love that touches me more nearly.
Loving offenders thus I will excuse ye,
Thou dost love her, because thou know’st I love her,
And for my sake even so doth she abuse me,
Suff’ring my friend for my sake to approve her.
If I lose thee, my loss is my love’s gain,
And losing her, my friend hath found that loss,
Both find each other, and I lose both twain,
And both for my sake lay on me this cross,
  But here’s the joy, my friend and I are one,
  Sweet flattery, then she loves but me alone."""


#szukanie słowa w linii
#for line in sonet42.splitlines():
#    for word in line.split():
#        #Srawdzamy, czy world jest rowne love
#        if word == 'love':
#            print(line)
        #Sprawdzamy, czy love jest w zbiorze slow love
#        if 'love' in word:
#
#            print(line)    

print(sonet42)
print(" ")
print("podaj słowo, któ©e chcesz wyszukać")
slowo = input()

for line in sonet42.splitlines():
    for slowo in line.split():
        #Srawdzamy, czy slowo jest rowne love
        if slowo == 'love':
            print(line)



            



    
