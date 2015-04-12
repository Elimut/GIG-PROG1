def funkce(retezec):
    prvky = retezec.split(" ")
    cislo1 = float(prvky[0])
    cislo2 = float(prvky[2])

    if prvky[1] == "+":
        vysledek = cislo1 + cislo2
    elif prvky[1] == "-":
        vysledek = cislo1 - cislo2
    elif prvky[1] == "*":
        vysledek = cislo1 * cislo2
    elif prvky[1] == "/":
        vysledek = cislo1 / cislo2
    elif prvku[1] == "**":
        vysledek = cislo1 ** cislo2
    else:
        raise NotImplementedError("Nerozpoznany operator")
    
    return(vysledek)

testRetezec = "45.4 / 51.8"
vysledek = funkce(testRetezec)
print(vysledek)
