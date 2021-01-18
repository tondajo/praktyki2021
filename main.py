
plik = open('dic\slowa.txt', 'r').read()
linie = plik.split('\n')

palindromy = []

def palindrom(linie):
    for slowo in linie:
        if (slowo != ""):
            if slowo == slowo[::-1]:
                palindromy.append(slowo)


    return palindromy

print(palindrom(linie))
print('W słowniku znajduje się ', len(palindromy), 'palindromów.')


