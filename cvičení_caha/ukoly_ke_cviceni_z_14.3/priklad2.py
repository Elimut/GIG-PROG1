vychoziHodnota = float(input("Zadej výchozí hodnotu: "))
koncovaHodnota = int(input("Koncova hodnota: "))

umocnenaHodnota = 1
i = 0

while umocnenaHodnota <= koncovaHodnota:
    umocnenaHodnota = umocnenaHodnota*vychoziHodnota
    i += 1

print("Čislo",vychoziHodnota, "je třeba umocnit",i,"krát než překročí hodnotu",koncovaHodnota)
