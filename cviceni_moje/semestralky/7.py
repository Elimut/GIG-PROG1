import sys 

if len (sys.argv) == 5: 

    vysledny_list = []

    soubor = open (sys.argv[1],"r") 
    retezec = soubor.readline()
    soubor.close()

    i = 0 

    while i < (len(retezec)-3):
        cifra = int(retezec [i]) + int(retezec[i + 1])*10 + int(retezec [i + 2])*100 + int(retezec [i + 3])*1000
        if cifra in vysledny_list: 
            pass 
        else: 
            if int(retezec[i + 3])>0:
                if int(sys.argv[3]) < cifra: 
                    if int(sys.argv[4]) > cifra:
                        vysledny_list.append(cifra) 

        i = i + 1 
    
    soubor = open (sys.argv[2],"w")
    
    for y in vysledny_list: 
        soubor.write(str(y) + "\n") 
    soubor.close()
        




