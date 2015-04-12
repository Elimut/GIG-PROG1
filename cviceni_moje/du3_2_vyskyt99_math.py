# Napište program, který načte soubor ukol_3_data.txt. Zkontrolujte si tento soubor.
# Soubor obsahuje n řetězců o 9 znacích oddělené oddělovačem.
# Vyberte z těchto řetězců všechny obsahující podřetězec „99“ (bez uvozovek) a uložte je do pole. Nakonec pole vytiskněte.
import random
import string

char_set = string.ascii_uppercase + string.digits
file = open("ukol_3_data.txt","w")
for i in range(1000):
    stringRandom = ''.join(random.sample(char_set*9, 9))
    string = stringRandom + ";"
    file.write(string)
file.close()

soubor = open("ukol_3_data.txt","r")
obsah = soubor.read()
retezce = obsah.split(";")

seznam = []
for retezec in retezce:
    if "99" in retezec:
        seznam.append(retezec)

print(seznam)

# Napište program, který načte soubor ukol_4_data.txt. Zkontrolujte si tento soubor. Soubor obsahuje n řádků s hodnotami x,y a z oddělené oddělovačem.
# Pro každý řádek spočítejte funkci sin(x) + cos(y) – log10(z). Výsledky ukládejte do pole a pole na závěr vytiskněte.
from random import random
file = open("ukol_4_data.txt","w")
for i in range(100):
    value1 = random()
    value2 = random()
    value3 = random()
    string = str(value1) + ";" + str(value2) + ";" + str(value3) +"\n"
    file.write(string)
file.close()

import math
soubor = open("ukol_4_data.txt","r")
radky =soubor.readlines()
soubor.close()
vysledky = []
for i in range(1,len(radky)):
    retezce = radky[i].split(";")
    x = float(retezce[0])
    y = float(retezce[1])
    z = float(retezce[2])    
    vysledek = math.sin(x) + math.cos(y) - math.log10(z)
    vysledky.append(vysledek)         
print(vysledky)


 
