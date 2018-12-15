#!/usr/bin/env bash

#grep -c -i Hamlet william.sheakspeare
#grep -c -i Macbeth william.sheakspeare
#grep -c -i Henry william.sheakspeare
#grep -c -i Ophelia william.sheakspeare
#grep -c -i Lady\ Macbeth william.sheakspeare

#definiujemy plik
text=william.sheakspeare

#definiujemy liste imion
names="Hamlet Macbeth Ophelia Henry"

#robimy petle po kolejnych imionach
for name in $names 
do
	echo -n  $name ": "
	 grep -E -c -i $name $text
done
