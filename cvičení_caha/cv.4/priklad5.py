def odstranZnaky(retezec):
    retezec = retezec.lower()
    ceskeZnaky = ["ě", "š", "č", "ř", "ž", "ý", "á", "í", "é", "ú", "ů", "ť", "ď", "ó", "ň"]
    asciiZnaky = ["e", "s", "c", "r", "z", "y", "a", "i", "e", "u", "u", "t", "d", "o", "n"]

    for i in range(len(ceskeZnaky)):
        retezec = retezec.replace(ceskeZnaky[i],asciiZnaky[i])

    return(retezec)    


testovaciRetezec = "Příšerně žluťoučký kůň úpěl ďábelské ódy."
print(testovaciRetezec)
vyslek = odstranZnaky(testovaciRetezec)
print(vyslek)
