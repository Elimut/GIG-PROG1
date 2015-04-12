import sys

if len(sys.argv) == 4:
    pole = []
    neparne = []
    parne = []
    vstup = open(sys.argv[1], "r")
    retazec = vstup.readline()
    vstup.close()

    i = 0
    while i < (len(retazec)-3):
        hodnota = int(retazec[i]) + int(retazec[i+1])*10 + int(retazec[i+2])*100 + int(retazec[i+3])*1000
        
        if int(retazec[i+3]) > 0:
            if int(sys.argv[3]) >= int(hodnota):
                pole.append(hodnota)
        i=i+1
        
    for x in pole:
        if int(x)%2 == 0:
            parne.append(x)
        else:
            neparne.append(x)
            
    vysledok = open(sys.argv[2], "w")
    for x1 in neparne:
        vysledok.write(str(x1) + "\n")
    for x2 in parne:
        vysledok.write(str(x2) + "\n")

    vysledok.close()
                 


