import sys
file = open(sys.argv[1],"r")

lines = file.readlines()

file.close()

cetnosti = []

for i in range(0,100):
    radek = []
    for j in range(0,100):
        radek.append(0)
    cetnosti.append(radek)
#print(cetnosti)

for i in range(0,len(lines)-1):
    cislo1 = int(lines[i])
    cislo2 = int(lines[i+1])
    cetnosti[cislo1-1][cislo2-1] =  cetnosti[cislo1-1][cislo2-1]+1
#print(cetnosti)

file2 = open(sys.argv[2],"w")
for i in range(0,100):
    for j in range(0,100):
        if (cetnosti[i][j]) != 0:
            retezec = str(i+1) + " " + str(j+1)+ " " + str(cetnosti[i][j]) + "\n"
            file2.write(retezec)
file2.close()


    
