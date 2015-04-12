import sys

vstup = sys.argv[1]
vystup = sys.argv[2]

soubor = open(vstup, 'r')
radky = soubor.readlines()
soubor.close()

delitel = int(sys.argv[3])
pole = []
for radek in radky:
    cislo = int(radek)
    if cislo == 0:
        continue
    if cislo%delitel == 0:
        pole.append(cislo)
        
file = open(vystup, 'w')
file.write('Nejmensi cislo delitelne bezezbytku cislem ' + str(delitel) + ' je: ' + str(min(pole)) + ' a nejvetsi: ' + str(max(pole)) + '.')
file.close()        

