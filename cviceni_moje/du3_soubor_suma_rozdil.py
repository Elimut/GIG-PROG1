# Napište program, který načte soubor ukol_1_data.txt. V souboru je n celých čísel z intervalu 1 – 1 000 000.
# Zjistěte počet čísel větších než 9 00 000 a sumu čísel menších než 1 000. Obě hodnoty vytiskněte na obrazovku.

from random import randint
file = open("ukol_1_data.txt","w")
for i in range(10000):
    string = str(randint(0,1000000)) + "\n"
    file.write(string)
file.close()

file = open("ukol_1_data.txt","r")
lines = file.readlines()
count = 0
sumValues = 0
for line in lines:
    value = int(line)
    if value > 900000:
        count  += 1
    if  value < 1000:
        sumValues += value
print("Pocet hodnot na 900 000 je", str(count))
print("Suma hodnota do 1 000 je", str(sumValues))

# Napište program, který načte soubor ukol_2_data.txt. Zkontrolujte si tento soubor.
# V souboru je n řádků obsahujících dvě desetinná čísla oddělená oddělovačem.
# Pro každý řádek zjistěte rozdíl cislo1 – cislo2.
# Spočte počet a celkovou sumu pro situace kdy je tento rozdíl kladný a zvlášť stejné charakteristiky pro záporný rozdíl.
# Na konci programu vytiskněte vhodné textové zhodnocení výsledků pro uživatele.
from random import random
file = open("ukol_2_data.txt","w")
delimiter = "%,%"
for i in range(10000):
    value1 = random()*1000
    value2 = random()*1000
    string = str(value1) + delimiter + str(value2) + "\n"
    file.write(string)
file.close()

soubor = open("ukol_2_data.txt","r")
radky =soubor.readlines()
soubor.close()

sumaKladna = 0
pocetKladnych = 0
sumaZaporna = 0
pocetZapornych = 0

for i in range(1,len(radky)):
    retezce = radky[i].split("%,%")
    rozdil = float(retezce[0])-float(retezce[1])

    if rozdil < 0:
        sumaZaporna += rozdil
        pocetZapornych += 1
    else:
        sumaKladna += rozdil
        pocetKladnych += 1
        
print("Kladnych rozdilu je",str(pocetKladnych),
      "a celkova suma techto rozdilu je", str(sumaKladna))
print("Zapornych rozdilu je",str(pocetZapornych),
      "a celkova suma techto rozdilu je", str(sumaZaporna))



