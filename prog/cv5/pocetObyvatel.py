file = open ("kraje.csv", "r")

lines = file.readlines()

pocetObyv = 0

for i in range(1,len(lines)):
    colums = lines[i].split(sep=";")
    pocetObyv += int(colums[3])
    print(colums)

print("Pocet obyvatel je: ",str(pocetObyv))
    
