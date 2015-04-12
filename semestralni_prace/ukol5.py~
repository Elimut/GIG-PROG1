import sys 

fileInput = open(sys.argv[1], 'r')
delitel = sys.argv[3]

listValues = []
for line in fileInput:
    value = int(line)
    if value == 0:
        continue
    remainder = value % int(delitel)
    if remainder == 0:
        listValues.append(value)

a = "nejmensi hodnota delitelna cislem " + delitel + " je: " + str(min(listValues))
b = "\n" + "nejvetsi hodnota delitelna cislem " + delitel + " je: " + str(max(listValues))

   
            
fileInput.close()

fileOutput = open(sys.argv[2], 'w')
fileOutput.write(a + b)
