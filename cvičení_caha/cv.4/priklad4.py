def znaky(retezec):
    if len(retezec) < 9:
        print("Operaci nelze provést")
    else:
        podretezec = retezec[4:9] 
        return(podretezec)

string = "01234567"
print(znaky(string))
