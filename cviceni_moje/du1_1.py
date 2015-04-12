# Od uživatele získejte vstupní hodnoty, které vymezují interval, v němž budete hledat řešení. Oba krajní body do tohoto intervalu budou patřit.
# Najděte všechny čísla celočíselně bezezbytku dělitelná 3 a současně i 8. A pro ty to hodnoty vytiskněte: Číslo x je dělitelné bezezbytku 3 i 8. Kde x je konkrétní číslo."

zacatek = int(input("Zadej počáteční hodnotu: "))
konec = int(input("Zadej koncovou hodnotu: "))

for i in range(zacatek, konec+1):
    zbytek3 = i % 3
    zbytek8 = i % 8
    if zbytek3==0 and zbytek8==0:
        print("Čislo",str(i), "je dělitelné bezezbytku 3 i 8.")

##########################
# Od uživatele získejte dvě vstupní hodnoty, kde první určuje číslo, které se bude umocňovat.
# Zjistěte, na kterou mocninu je třeba umocnit první vstupní hodnotu, aby byla striktně větší než druhé zadané číslo. 
# Příklad: vstupy 2 a 9. 24(=16)>9, naproti tomu 23(=8)<9, takže výsledkem je 4.

vychoziHodnota = float(input("Zadej výchozí hodnotu: "))
koncovaHodnota = int(input("Koncova hodnota: "))

umocnenaHodnota = 1
i = 0

while umocnenaHodnota <= koncovaHodnota:
    umocnenaHodnota = umocnenaHodnota*vychoziHodnota
    i += 1

print("Čislo",vychoziHodnota, "je třeba umocnit",i,"krát než překročí hodnotu",koncovaHodnota)

##########################
# Projděte interval čísel od 1000 do 450 s krokem -10 a zjistěte počet čísel dělitelných celočíselně číslem 16 ze zbytkem právě 8.
# Netiskněte čísla, pouze na závěr jejich počet.

count = 0
for x in range(1000,440,-10):
    if (x%16)==8:
        count += 1
        #print(x)
print("Čísel existuje celkem ", count,".", sep="")

##########################
#  Vytiskněte 15 řádků, na každém řádku bude právě 15 znaků.
# První řádek bude začínat jednou * a bude následovat čtrnáct /, na každém řádku pak přibude jedna * a ubyde jedno /.
#Poslední řádek budou pouze *.

for x in range (0,15):
    for y in range (0,15):
        if y<=x:
            print("*",end="")
        else:
            print("/",end="")
    print()

##########################
# Zjistěte zda-li v intervalu zadaném od uživatele lze najít číslo, které je dělitelné bezezbytku 17 a zároveň i 14.
# Pokud ano, vypište, že číslo bylo nalezeno. Pokud ne, pokuste se takové číslo najít v intervalu, který bude rozšířený na obě strany o 50.
# Pokud tam hodnota existuje, vypište, že číslo lze najít v rozšířeném intervalu. Pokud ani tam řešení není, pak vypište, že hodnotu nelze najít.

a = int(input("Zadej jednu hranici intervalu:"))
b = int(input("Zadej druhou hranici intervalu:"))

found = False

for x in range(a,b):
    if x%17==0 and x%14==0:
        found = True
        print(x)

if found:
    print("Hodnota existuje.")
else:
    for x in range(a-50,b+50):
        if x%17==0 and x%14==0:
            found = True
    if found:
        print("Hodnota existuje v rozšířeném intervalu.")
    else:
        print("Hodnota neexistuje ani v rozšířeném intervalu.")





















