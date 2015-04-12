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
    
