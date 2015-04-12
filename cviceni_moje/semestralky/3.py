import sys

vstup = open(sys.argv[1], "r")
vystup = open(sys.argv[2], "w")
soubor = vstup.read()
vstup.close()
soubor = soubor.split("\n")  

soubor.remove("")
for i in range(0,len(soubor)):
        soubor[i] = int(soubor[i])
   
        
          
"""prevede jednotlive prvky v souboru na intenger
jak udelat aby to odchytilo prazdne misto v prubehu seznamu a ingnorovalo ho?"""

sezDvoj = []
pocetDvoj=[]

for i in range(0,len(soubor)):
        dvojice = soubor[i:i+2]
        sezDvoj.append(list(dvojice))    

""" nacteni souboru do seznamu
a jeho roztrideni do dvojic => vznik seznamu v seznamu"""

for n in range(0,len(sezDvoj)):
    pocet = sezDvoj.count(sezDvoj[n])
    pocetDvoj.append((pocet))

""" zjisteni poctu stejnych prvku v souboru """

for m in range(0, len(sezDvoj)):
    dvojice1 = sezDvoj[m]
    mnozstvi = pocetDvoj[m]
    dvojice1.append(mnozstvi)
sezDvoj.pop()       #odstrani posledni cislo ze seznamu 

""" spojeni sezDvoj s pocetDvoj"""

if sezDvoj:
    sezDvoj.sort()  #seradi prvky
    posledni = sezDvoj[-1]
    for i in range(len(sezDvoj)-2, -1, -1):
        if posledni == sezDvoj[i]:
            del sezDvoj[i]
        else:
            posledni = sezDvoj[i]

"""mazani duplicit a serazeni"""

vystup.write("x y f(x,y)"+"\n")
for p in range(0,len(sezDvoj)):
    for r in range(0,len(sezDvoj[0])):
        vystup.write(str(sezDvoj[p][r])+" ")
    vystup.write("\n")

"""konverze a vypis do textaku"""
    
vystup.close()
    
        


            


            







    
   
    


    












    
