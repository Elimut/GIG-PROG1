# Napište program, který vygeneruje soubor ukol_1_data.txt.
# Soubor bude obsahovat hlavičku uniform;gauss;lognormvariate a následně 1 000 řádků,
# s náhodnými čísly vygenerovanými ze zadaných rozdělení
#(parametry rozdělení jsou na vás, nepožadují se žádné konkrétní). Oddělovačem hodnot bude středník.
import random

file = open("ukol_1_data.txt","w")
string = "uniform;gauss;lognormvariate\n"
for i in range(1000):
    uniform = random.uniform(0,1000)
    gauss = random.gauss(500,125)
    lognormal = random.lognormvariate(0,8)
    string +=  str(uniform) + ";" + str(gauss) + ";" + str(lognormal) + "\n"

file.write(string)
file.close()

# Napište program, který načte soubor ukol_2_data.txt.
# Z datasetu vyseparujte do seznamu čtvrtý sloupec hodnot.
# Tento seznam vytiskněte do souboru ukol_2_4_sloupec.txt tak, že na každém řádku bude právě jedna hodnota.
soubor = open("ukol_2_data.txt","r")
radky = soubor.readlines()
soubor.close()

seznam = []
for radek in radky:
    retezce = radek.split(" ")
    seznam.append(float(retezce[3]))

souborNovy = open("ukol_2_4_sloupec.txt","w")
for zaznam in seznam:
    souborNovy.write(str(zaznam)+"\n")
souborNovy.close()

 # Napište funkci, která má tři argumenty – první je název souboru v textové podobě, druhý parametr je booleovská hodnota a třetí je index.
 # Funkce načte soubor, pokud je booleovská hodnota True, pak načte data z řádku definovaného třetím argumentem.
 # Pokud je tato hodnota False, pak funkce načte sloupec s příslušným indexem.
 # Funkce v obou případech vrací seznam čísel s plovoucí desetinnou čárkou.
def extrahujData(nazevSouboru, radekSloupec, cislo):
    soubor = open(nazevSouboru,"r")
    radky = soubor.readlines()
    
    if radekSloupec:
        seznam = radky[cislo].split(" ")
        seznam.remove("\n")
        #print(seznam)
        data = []
        for zaznam in seznam:
            data.append(float(zaznam))  
    else:
        data = []
        for radek in radky:
            seznam = radek.split(" ")
            data.append(float(seznam[cislo]))

    return(data)
    
#dataSet = extrahujData("ukol_2_data.txt", False, 1)
#print(dataSet)


# Ze souboru v Úkolu 3 si naimportujte vytvořenou funkci. Funkci zavolejte s parametry ("ukol_2_data.txt", False, 55) .
# Seznam hodnot vytiskněte na obrazovku.
# V seznamu, který funkce vrátí zjistěte nejmenší a největší hodnotu a jejich indexy v rámci seznamu.
from ukol3 import extrahujData

data = extrahujData("ukol_2_data.txt", False, 55)
print(data)

minimum = float("inf")
minIndex = 0
maximum =  float("-inf")
maxIndex = 0

for i in range(0,len(data)):
    if data[i] < minimum:
        minimum = data[i]
        minIndex = i
    if data[i] > maximum:
        maximum = data[i]
        maxIndex = i


print("Minimum je",minimum,"na pozici",minIndex)
print("Maximum je",maximum,"na pozici",maxIndex)



# Ze souboru v Úkolu 3 si naimportujte vytvořenou funkci. Funkci zavolejte s parametry ("ukol_2_data.txt", True, 100).
# V seznamu, který funkce vrátí zjistěte počet hodnot 0 a 1, dále počet hodnot větších než 0.5
# ale nerovnajících se 1 a všech ostatních, které nevyhovují ani jedné z těchto tří podmínek.
# Pro každý počet hodnot vytiskněte informaci: Počet hodnot x je y což je z % z celkového počtu.
from ukol3 import extrahujData

data = extrahujData("ukol_2_data.txt", True, 100)

pocet0 = 0
pocet1 = 0
pocetNad05 = 0
pocetOstatni = 0

for hodnota in data:
    if hodnota == 0:
        pocet0 += 1
    elif hodnota == 1:
        pocet1 += 1
    elif hodnota > 0.5:
        pocetNad05 += 1
    else:
        pocetOstatni += 1

#hodnot = pocet0 + pocet1 + pocetNad05 + pocetOstatni
hodnot = len(data)
procenta0 = (pocet0 / hodnot)*100
procenta1 = (pocet1 / hodnot)*100
procenta05 = (pocetNad05 / hodnot)*100
procentaOstatni = (pocetOstatni / hodnot)*100

print("Počet hodnot 0 je", pocet0,"což je",procenta0,"% z celkového počtu.")
print("Počet hodnot 1 je", pocet1,"což je",procenta1,"% z celkového počtu.")
print("Počet hodnot nad 0.5 je", pocetNad05,"což je",procenta05,"% z celkového počtu.")
print("Počet ostatních hodnot je", pocetOstatni,"což je",procentaOstatni,"% z celkového počtu.")
