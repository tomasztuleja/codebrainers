#!/usr/bin/env bash
mkdir -p 2018.12.15.cwiczenia
cd 2018.12.15.cwiczenia

echo "To jest nasz skrypt"

# dwa >> zapisuja kolejna linijke w pliku, pojedynczy > nadpisuje plik
echo 'A to zostanie zapisane w pliku stdout.txt o godzinie ' $(date) >> stdout.txt

echo "Sprawdzam, czy rzeczywiście plik stdout.txt zawiera nasz napis"


date

more stdout.txt
