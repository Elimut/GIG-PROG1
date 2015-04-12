import sys                                                          #System-specific parameters and functions

def FileWrite(pole):                                                #funkce pro zapis promněnné pole do souboru na adrese druhého argumentu
    vysledek=open(sys.argv[2], mode="w")                            # otevreni souboru pro zapis
    for i in range(0,len(pole),3):
            vysledek.write(str(pole[i])+"\t"+str(pole[i+1])+"\t"+str(pole[i+2])+"\n")
    vysledek.close()

def FindMax(pole):                                                  #funkce pro vyhledání maxima v poli a jeho zapsání na konec pole
    MAX=0
    MAXindex=0
    for i in range(2,len(pole),3):                                  # prochazí list=[2,5,8,11,14...]
        if(pole[i]>MAX):
            MAXindex=i-2                                            #index souradnice x
            MAX=pole[i]
    pole.extend((pole[MAXindex],pole[MAXindex+1],pole[MAXindex+2])) #LIST EXTEND rozsireni pole o radek z nejvyssi cetnosti
    return pole

def Freq(file):
    pole=[]                                                         #definice pole
    y=int(-1)                                                       #prirazeni hodnoty -1 do promenne y y duvodu detekce prvniho nacteni
    for line in file:
        x=y
        y=int(line)
        if x==-1:
            continue                                                #FLOW CONTROL pusti dalsi interaci cyklu
        if(y==50):
            if(x in pole[0::3]):                                    # LIST SELECT vsechny treti prvky
                for i in range(0,len(pole),3):                      #procházení vysledneho pole cyklus y range pouzit kvuli indexu
                    if(pole[i]==x):
                        pole[i+2]=pole[i+2]+1                       # přičítání četností u stejných x
                        break                                       #FLOW CONTROL vyskoci z nadrazeneho cyklu
            else:
                pole.extend((x,y,1))                                #LIST EXTEND rozsireni pole o novy prvek (x,y,cetnost)
    return pole

def main():
    if(len(sys.argv)>=3):                                           #zjistuje zda je dostatek parametru
        vstup = open(sys.argv[1])                                   #otevření souboru pro čtení bez ověření ,že existuje --> import os.path \n if(os.path.isfile(adresa))
        cetnost=Freq(vstup)
        vstup.close()
        FileWrite(FindMax(cetnost))
        #print("Soubor vysledku byl ulozen do "+sys.argv[2]+"...")
    else:                                                           #pokud není dost parametru vypíše hlašku
        print("Nedostatek parametru nemohu provest operace")        #možnost rekurzivního zavolání funkce main ze zadáním chybějcích informací
  
main()
