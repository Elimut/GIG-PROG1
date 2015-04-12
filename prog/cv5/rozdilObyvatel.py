file = open ("kraje.csv", "r")

lines = file.readlines()

pocetObyv = 0

for i in range(1,len(lines)):
    colums = lines[i].split(sep=";")
    rozdil = int(colums[3]) - int(colums[4])
    print(colums[2]," ",rozdil)
    pocetObyv += rozdil

print("Rozdil obyvatel je: ",str(pocetObyv))
    
