def vytvorPole(N, M):
    hodnota = 515
    pole = []
    for i in range(0,N):
        radek = []
        for j in range(0,M):
            radek.append(hodnota)
            hodnota = hodnota + 6
        pole.append(radek)
        
    return(pole)

def vyplnPole(pole):
    hodnota = 300
    for i in range(0,len(pole)):
        for j in range(0,len(pole[1])):
            nalezeno = False
            while nalezeno == False:
                if hodnota%4==0 and hodnota%7==0:
                    nalezeno = True
                    pole[i][j] = hodnota
                hodnota = hodnota + 1

pole = vytvorPole(5,9)
vyplnPole(pole)
print(pole)
