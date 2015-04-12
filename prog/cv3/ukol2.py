#napiste program ktery od uzivatele ziska vstupy. Pocet radku k tisteni a pocet cisel na radku. Vytisknete pro kazdy radek posloupnost 1 - pocet prvku

radek = int(input("Zadej pocet radku: "))
sloupec = int(input("Zadej pocet cisel na radku: "))
for i in range (0, radek):
    for x in range (1, sloupec+1):
         print(x, end=" ")
    print()
