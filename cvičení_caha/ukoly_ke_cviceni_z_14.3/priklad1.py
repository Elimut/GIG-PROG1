zacatek = int(input("Zadej počáteční hodnotu: "))
konec = int(input("Zadej koncovou hodnotu: "))

for i in range(zacatek, konec+1):
    zbytek3 = i % 3
    zbytek8 = i % 8
    if zbytek3==0 and zbytek8==0:
        print("Čislo",str(i), "je dělitelné bezezbytku 3 i 8.")
