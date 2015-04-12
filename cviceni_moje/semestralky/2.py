import sys
vstup=open(sys.argv[1],"r")
vystup=open(sys.argv[2],"w")

for cislo in vstup:
    radek=cislo.split(".")
    if int(radek[0])<=200 and int(radek[3])%7==0:
        vystup.write(cislo)
                                        
vstup.close()
vystup.close()



                    
        
    
    

