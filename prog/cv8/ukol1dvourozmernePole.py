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

pole = vytvorPole(4,2)
print(pole)
