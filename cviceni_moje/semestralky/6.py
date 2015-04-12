import sys

if len(sys.argv) == 3:
    
    pole = []
    suma = 0
    pocet = 0
    odchylka = 0
    soubor=open(sys.argv[1],"r")
    for i in soubor:
        pole.append(int(i))
        suma = suma+int(i)
        pocet = pocet+1
    prumer = suma/pocet
    for i in pole:
        
        odchylka = odchylka + (int(i) - prumer)*(int(i) - prumer)
        
    soubor.close()
        
    smerodatnaOdchylka = ((1 / pocet) * int(odchylka))**(1/2)
    
    soubor=open(sys.argv[2], "w")
    soubor.write("Prumer: " + str(prumer)+ "\nSmerodatna odchylka: "+ str(smerodatnaOdchylka))
else:
    print("Neplatny pocet parametru.")
