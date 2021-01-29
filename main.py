import time

linie = []
palindromy = []


def reverse(slowo):
    odwroconeslowo = ''
    for litera in slowo:
        odwroconeslowo = litera + odwroconeslowo
    return odwroconeslowo


def palindrom(linie):
    with open('dic\slowa.txt', "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        for slowo in linie:
            if reverse(slowo) == slowo:
                palindromy.append(slowo)
    return palindromy


def main():
    przed = time.perf_counter()
    print('Znalezione palindromy:', palindrom(linie))
    print('W słowniku znajduje się ', len(palindromy), 'palindromów.')
    po = time.perf_counter()
    print(f"Znaleziono w {po - przed:0.4f} sekund")



if __name__ == "__main__":
    main()







