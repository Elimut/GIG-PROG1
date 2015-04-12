import sys

pocetArgumentu = len(sys.argv)

if pocetArgumentu < 3:
    print ("Prilis malo argumentu.")
elif pocetArgumentu == 3:
    vysledek = float(sys.argv[1]) * float(sys.argv[2])
    print("vysledek je ",vysledek)
else:
    print("Az moc argumentu.")
