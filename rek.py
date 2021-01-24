
import time

plik = open('dic\slowa.txt', 'r').read()
linie = plik.split('\n')

palindromy = []

def palindrom(slowo):
    if len(slowo) < 1:
        return True
    else:
        if slowo[0] == slowo[-1]:
            return palindrom(slowo[1:-1])
        else:
            return False

przed = time.perf_counter()
for slowo in linie:
    if (slowo != ""):
        if(palindrom(slowo)==True):
            palindromy.append(slowo)
po = time.perf_counter()

print(f"Znaleziono w {po - przed:0.4f} sekund")
print('Znalezione palindromy:', palindromy)
print('W słowniku znajduje się ', len(palindromy), 'palindromów.')


