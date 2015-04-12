file = open ("vystup.txt", "w")

for i in range(10):
    string = str(i) + "\n"
    file.write(string)
    
file.close()
