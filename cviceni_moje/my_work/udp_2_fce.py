def not_to_do():
    pass # -> prázdná operace 
# funkce, která nic nedělá.

##### dokumentační řetězec #####
def deleni(x,y):
    """ vrátí výsledek po celočíselném dělení a taky jeho zbytek """
    # vlastně se ten dok. řetězec dá použít i místo pass
    return x // y, x % y
print(deleni(17,4)) # (4,1)

print(deleni.__doc__) #dokumentační řetězec, jedna z magických fcí

##### poziční argumenty #####
def f(a,b):
    print("\nArgument 1: " + str(a)) #samozřejmě to jde napsat i "obyčejně", než zřetězením
    print("Argument 2: " + str(b))
    
f(1,2)
#f('blah', 5)
#f(5, ('foo', 'bar'))

 

