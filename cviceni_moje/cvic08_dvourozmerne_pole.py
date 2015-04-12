def fce(N,M):
    hodnota = 515
    pole=[]
    for x in range(0,N): #prochází sloupce
        radek=[]
        for i in range(0,M): #tvoří řádek 
            radek.append(hodnota)  #přidává hodnoty na radek
            hodnota = hodnota + 6
        pole.append(radek)   #pridává 
    return(pole)

def fce2(pole):
    hodnota = 300
    for j in range(0,len(pole[0])):
        for i in range(0,len(pole)):
            nalezeno = False
            while nalezeno==False:
                if hodnota%4==0 and hodnota%7==0:
                    pole[i][j] = hodnota
                    nalezeno = True
                hodnota = hodnota + 1

def fce3(pole):
    for i in range(0,len(pole)):
        for j in range(0,len(pole[0])):
            print(pole[i][j], end="\t")
        print("",end="\n")


pole = fce(10,3)
fce2(pole)
fce3(pole)
