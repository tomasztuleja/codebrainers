#!/usr/bin/env python

def word_search(slowo, gdzie):

    for line in gdzie:
        for word in line.split():
            #Srawdzamy, czy slowo jest rowne love
            if slowo in word:
                print(word, line)    



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

print("Podaj słowo: ")
do_wyszukania = input()

print("Podaj nazwe pliku")
nazwa_pliku = input()


with open(nazwa_pliku, "r") as plik:
    word_search(do_wyszukania, plik.readlines())



               
