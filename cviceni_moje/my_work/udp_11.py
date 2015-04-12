""" zpracování vstupu
    1) přímý vstup z klávesnice do běžícího programu
    2) vstup do programu v podobě parametrů
    """

""" zpracování parametrů skriptu:
    0) sys.argv - přístup k parametrům skriptu na nejnižší úrovni
    1) getop
    2) optparse
    3)argparse
"""

import sys
if len(sys.argv) <= 1:
    print("Usage: {} ARGUMENT".format(sys.argv[0]))
    sys.exit()

""" pozičních argumentů nemusí být doptředu známý počet - všechny přebytečné schroustne v podobě tuplu
speciální argument s operátorem *, který způsobí rozbalení předaných hodnot do n-tice """

def f(arg1, arg2, *args):
    print("argument 1: " ,arg1)
    print("argument2: " ,arg2)
    print("další argumenty: " ,args)
print(f(1,2,3,4,5,6))
