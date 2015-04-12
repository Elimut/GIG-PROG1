from random import randint

file = open("ukol_1_data.txt","w")

for i in range(10000):
    string = str(randint(0,1000000)) + "\n"
    file.write(string)

file.close()
    
