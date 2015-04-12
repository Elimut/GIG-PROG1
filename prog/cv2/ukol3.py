import sys
pocetargumentu = len(sys.argv)
if pocetargumentu < 3:
    print("Prilis malo argumentu.")
elif pocetargumentu == 3:
    vysledek = float(sys.argv[1]) * float(sys.argv[2])
    print("Vysledek je: ",vysledek)
else:
    print("Prilis moc argumentu.")
