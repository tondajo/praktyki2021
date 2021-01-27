import time

linie = []
palindromy = []

def palindrom(linie):
    with open('dic\slowa.txt', "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        przed = time.perf_counter()
        for slowo in linie:
            if slowo != "":
                if slowo == slowo[::-1]:
                    palindromy.append(slowo)
        po = time.perf_counter()
        print(f"Znaleziono w {po - przed:0.4f} sekund")
    return palindromy


def main():
    print('Znalezione palindromy:', palindrom(linie))
    print('W słowniku znajduje się ', len(palindromy), 'palindromów.')



if __name__ == "__main__":
    main()


