"""
/// pravdivostní hodnoty objektů ///
- false (cokoliv jiného než true) je:
  - None, False
  - nula (int, long, float)
  - prázdná sekvence('', (), [])
  - prázdné mapování ({})
"""

xl = 'abcdefghchijklmno'
'd' in xl #true
'd' not in xl #false


##### decimal #####
# je to supr věc, můžu si zvolit přesnost výpočtů jakou chci
import decimal
D = decimal.Decimal
a = D(1)/D(7) #0.1428571428571428571428571429
print(a)

decimal.getcontext().prec = 5
# decimal.getcontext() vrací aktuální nastavení
print(D(1)/D(7)) #0.14286
decimal.getcontext().prec = 28

D(str(3 * 0.1)) - D('0.3') #0.0 (bez decimal by to vyhodilo komplexní číslo, což nemáme rádi a nechceme
D('1.30') + D('1.20') #2.50 -> drží nastavený počet významných míst
D('-Infinity') + D('-Infinity') #-Infinity
D(1).exp() #Decimal('2.718281828459045235360287471')
#umi i treba ln nebo sqrt

##### fractions #####
import fractions
#dalsi supercool vec, umi pracovat se zlomky
F = fractions.Fraction
F('-16/10') + F('3/5') #Fraction(-1/1)
fractions.gcd(42, 56) #42 -> největší společný dělitel



