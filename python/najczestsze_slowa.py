#!/usr/bin/env python

f = open("proust.txt")

text = f.read()

# Lista slow z pliku txt
w = text.split()

dic = {}

for word in w:
    word.lower().strip(".?,!-=_;") # male litery i czyszczenie ze znaków specjalnych na krańcach stringa
    if word not in dic: 
        dic[word] = 1
    else:
        dic[word] += 1

#print(dic)

dic2 = {} 

#Rozwiązanie
for kword, f in dic.items(): #dic.items() to inaczej f = freq[kword]
    if f in dic2:
        dic2[f].append(kword)
    else:
            dic2[f] = [kword]
#Moja próba:
#for klucz in dic:
#    val = dic[klucz]
#    dic2[val] = klucz.append(klucz)

print(sorted(dic2.items()))

###########################
#s = set(w)

# Lista unikalnych slow
#l = list(s)

#for i in l:
#    for j in w:
#        if j in i

#print(len(w), len(s), len(l))