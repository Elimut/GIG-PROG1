cisla = [7,9,2,4,8,9,10]

suma = 0

for cislo in cisla:
    if cislo%2 == 0:
        continue
    suma += cislo
   
print(suma)
