
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

for slowo in linie:
    if(palindrom(slowo)==True):
        palindromy.append(slowo)

print(palindromy)
print('W słowniku znajduje się ', len(palindromy), 'palindromów.')

