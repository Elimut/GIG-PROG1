import string
import random

char_set = string.ascii_uppercase + string.digits
file = open("nahretez.txt","w")

for i in range(1000):
    stringRandom = "".join(random.sample(char_set*9,9))
    string = stringRandom + ";"
    file.write(string)

file.close()
