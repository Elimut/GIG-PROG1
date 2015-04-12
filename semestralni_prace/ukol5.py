import sys 

fileInput = open(sys.argv[1], 'r') #prvni argument = vstupni soubor
delitel = sys.argv[3] #treti argumet = delitel

listValues = [] #zalozeni pole na ukladani
for line in fileInput:
    value = int(line) #pretypovani
    if value == 0: #nulu nechci
        continue
    remainder = value % int(delitel) #zbytek po deleni tretim vstupnim argumentem
    if remainder == 0: #pokud je zbytek po deleni roven nule
        listValues.append(value) #tak hodnotu pridej do pole

a = "nejmensi hodnota delitelna cislem " + delitel + " je: " + str(min(listValues)) #tisk nejmensi hodnoty delitelne delitelem
b = "\n" + "nejvetsi hodnota delitelna cislem " + delitel + " je: " + str(max(listValues)) #tisk nejvetsi hodnoty delitelne delitelem

   
            
fileInput.close() #zavri vstupni soubor!

fileOutput = open(sys.argv[2], 'w') #otevri vystupni soubor = druhy argument
fileOutput.write(a + b) #zapis do vystupniho souboru nejmensi a nejvetsi hodnotu
