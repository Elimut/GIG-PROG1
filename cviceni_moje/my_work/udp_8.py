
# f = open('cesta/k/souboru', mode='r', encoding='utf-8')
# ...
# f.close()

### stačí mít otevřený stream, kdy kod v bloku proběhne at už úspěšně nebo neúspěšně, tak je stream automaticky uzavřen
# with open('ukol_2_data.txt, encoding='utf-8') as f:
# BLOK

f = open('ukol_2_data.txt')
dir(f) # zase chytré metody
f.name #název

""" mody otevření souboru -
    r - soubor je otevřen pouze pro čtení
    w - pro zápis (již existující neprázdný soubor bude smazán)
    a - soubor je otevřen pro přidávání (přidání dat na konec)
    r+ - pro čtení i zápis
    w+ - pro čtení i zápis (již existující neprázdný soubor bude smazán)
    """

##### čtení ze streamu #####
"""
- načtení celého streamu najednou:
    - content = stream.read()
    - zavolání read() bez parametrů je ekvivalentní s readall()

- načtení souborů klasicky po řádcích
    - soubor = open('soubor.txt')
    - for line in file:
        BLOK
    - for (number, line) in enumerate(file):
        BLOK
- nebo po blocích řádek
    
    f = soubor('soubor.txt')
    f.readline() <- načteme ze souboru všechny řádky
    f.seek(0) <- vrátíme se na začátek
    for line in f.readlines():
        print(line) <-proiterujeme pres seznam
    blablabla....
    na konci zavřeme soubor f.close() """""

##### zápis do streamu #####
f = open('test', 'w')
f.write('Ahoj, světe!') # <- vrací počet zapsaných znaků (12)
f.write('Jak se máš?')#  <- (11)
f.close()

# koukneme se co jsme si zapsali --
f = open('test', 'r')
print(f.read())
f.close()


