
"spočítat celkovou sumu obyvatel pro čr a vytisknout ji na obrazovku"
file = open("kraje.csv", "r")

lines = file.readline()

pocetObyvatel = 0

for i in range(1, len(lines)):
    columns = lines[i].split(sep=";")
    pocetObyvatel += int(columns[3])
print("pocet obyvatel je" ,str(pocetObyvatel))

"počítat rozdíly počtu obyvatel mezi roky 91 a 01"
file = open ("kraje.csv", "r")
lines = file.readlines()
pocetObyv = 0

for i in range(1,len(lines)):
    colums = lines[i].split(sep=";")
    rozdil = int(colums[3]) - int(colums[4])
    print(colums[2]," ",rozdil)
    pocetObyv += rozdil

print("Rozdil obyvatel je: ",str(pocetObyv))

"argumenty: seznam radku ze souboru a cisla dvou sloupcu mezi kterými má spočítat rozdíl. spočítejte rozdíl pro každý řádek ze souboru a uložte do pole, které fce vrací"
def rozdilSloupcu(radky, indexS1, indexS2):
    rozdily = []
    for radek in radky:
        hodnoty = radek.split(sep=";")
        rozdil = float(hodnoty[indexS1]) - float(hodnoty[indexS2])
        rozdily.append(rozdil)
    return(rozdily)  

soubor = open ("cisla.txt", "r")
radky = soubor.readlines()
rozdilyCisel = rozdilSloupcu(radky,0,2)
print(rozdilyCisel)
    
