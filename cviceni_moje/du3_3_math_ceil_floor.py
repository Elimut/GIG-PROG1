# Napište program, který načte soubor ukol_5_data.txt.
# Zkontrolujte si tento soubor. Soubor obsahuje n řádků s hodnotou.
# Pro každý řádek zjistěte hodnotu nejmenšího celého čísla většího nebo rovno než hodnota na řádku, a hodnotu největšího celého čísla menšího nebo rovno hodnotě na řádku.
# Výsledné hodnoty zapište do souboru ukol_5_vysledek.txt ve formátu mensi;vetsi. Každému řádku původního soboru odpovídá řádek nového souboru.
from random import random
file = open("ukol_5_data.txt","w")
for i in range(200):
    string = str(random()*9999) + "\n"
    file.write(string)
file.close()

import math
soubor = open("ukol_5_data.txt","r")
radky =soubor.readlines()
soubor.close()
vysledky = []
for i in range(1,len(radky)):
    hodnota = float(radky[i])
    mensi = math.floor(hodnota)
    vetsi = math.ceil(hodnota)
    vysledky.append([mensi, vetsi])

retezec = ""
for vysledek in vysledky:
    retezec += str(vysledek[0])+";"+str(vysledek[1])+"\n"

souborNovy = open("ukol_5_vysledek.txt","w")
souborNovy.write(retezec)
souborNovy.close()
