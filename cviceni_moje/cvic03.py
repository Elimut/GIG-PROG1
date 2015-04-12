
"vytiskne pro každý řádek posloupnost 0 - počet prvků"
pocetRadku = int(input("zadejte pocet radku: "))
pocetPrvku = int(input("zadejte pocet prvku: "))

for i in range (0, pocetRadku):
    for j in range (0, pocetPrvku):
        print(j, end = " ")
    print()

"program, který jako vstup získá počet řádků. pro každý řádek tiskne hodnoty podle vzoru"
" 1, 22, 333"
for i in range (1, (pocetRadku+1)):
    for j in range (1, i+1):
        print(i, end = " ")
    print()

"vytiskne příslušný počet řádků s odpovídajícím počtem prvků"
pocetRadku = int(input("zadejte pocet radku: "))
pocetZnaku = int(input("zadejte pocet znaku na radku: "))

for i in range (0, pocetRadku):
    for j in range (0, pocetZnaku):
        value = i * pocetZnaku + j
        print(value, end = " ")
    print()























                       
