
import time

plik = open('dic\slowa.txt', 'r').read()
linie = plik.split('\n')

palindromy = []

def palindrom(linie):
    przed = time.perf_counter()
    for slowo in linie:
        if (slowo != ""):
            if slowo == slowo[::-1]:
                palindromy.append(slowo)
    po = time.perf_counter()
    print(f"Znaleziono w {po - przed:0.4f} sekund")
    return palindromy

print(palindrom(linie))
print('W słowniku znajduje się ', len(palindromy), 'palindromów.')

