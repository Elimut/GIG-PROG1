def znaky(retezec):
    if len(retezec) < 9:
        print("Nelze")
    else:
        podretezec = retezec[4:9]
        return(podretezec)
    
string = "0123456789"
print(znaky(string))
