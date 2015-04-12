from random import random

file = open("ukol_2_data.txt","w")

delimiter = "\_/"

for i in range(10000):
   value1 = random()*1000
   value2 = random()*1000
   string = str(value1) + delimiter + str(value2) + "\n"
   file.write(string)
 
file.close()
    
