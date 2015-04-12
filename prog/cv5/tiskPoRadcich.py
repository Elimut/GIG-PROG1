file = open ("kraje.csv", "r")

fileContent = file.readlines()

for line in fileContent:
    print(line)
    
file.close()
