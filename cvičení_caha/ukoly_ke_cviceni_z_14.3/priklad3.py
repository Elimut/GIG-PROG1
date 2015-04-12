count = 0
for x in range(1000,440,-10):
    if (x%16)==8:
        count += 1
        #print(x)
print("Čísel existuje celkem ", count,".", sep="")
