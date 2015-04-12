def retezecSeznam(l, s):
    seznam = []
    for retezec in l:
        if s in retezec:
            seznam.append(retezec)
    return(seznam)


seznam = ["test1", "test2", "test3", "test4", "test5", "test6",]
retezec = "test1"
print(retezecSeznam(seznam, retezec))
