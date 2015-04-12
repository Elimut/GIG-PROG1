import sys

pocetArgumentu = len(sys.argv)

if pocetArgumentu < 3:
    print("Prilis malo argumentu.")
elif pocetArgumentu == 3:
    vysledek = float(sys.argv[1]) * float(sys.argv[2])
    print("Vysledek je ",vysledek)
else:
    print("Prilis mnoho argumentu.")
