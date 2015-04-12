#napiste program ktery od uzivatele ziska jako vstup pocet radku. Pro kazdy radek tisknete hodnoty dle vzoru.

radek = int(input("Zadej pocet radku: "))
for i in range (1, radek+1):
    for x in range(0,i):
        print(i, end=" ")   
    print()
