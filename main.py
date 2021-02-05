import time
import argparse

linie = []
palindromy = []
palindromy_2 = []


wyświetlanie = ""
czas = ""
funkcja = ""

def parseArguments():
    parser = argparse.ArgumentParser(description='Wyszukiwanie palindromów')
    parser.add_argument('--wyświetlanie', '-w', action='store_true', help='Umożliwia wyświetlanie wyszukanych palindromów')
    parser.add_argument('--czas', '-c', type=str, help='Umożliwia wyświetlanie czasu wykonania programu: tak/nie', )
    parser.add_argument('--funkcja', '-f', type=str, help='Wybiera w jaki sposób zostanie wykonany program: 1/2', )
    parser.add_argument('--plik', '-p', type=str, help='Wybiera plik ze słownikiem: (ścieżka do pliku)', required=True, )
    args = parser.parse_args()
    return args

def elementyListy(lista):
    x = 0
    for element in lista:
        x += 1
    return x


def wyszukiwaniePalindromow(linie, args):
    with open(args.plik, "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        for slowo in linie:
            if slowo != "":
                if slowo == slowo[::-1]:
                    palindromy.append(slowo)
    return palindromy

def reverse(slowo):
    odwroconeSlowo = ''
    for litera in slowo:
        odwroconeSlowo = litera + odwroconeSlowo
    return odwroconeSlowo


def wyszukiwaniePalindromow_2(linie, args):
    with open(args.plik, "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        for slowo in linie:
            if reverse(slowo) == slowo:
                palindromy_2.append(slowo)
    return str(palindromy_2)


def main(args):
    palindromy = wyszukiwaniePalindromow(linie, args)
    przed = time.perf_counter()
    print('W słowniku znajduje się ', len(palindromy), 'palindromów.')
    if args.wyświetlanie:
        if args.funkcja == '1':
            print('Znalezione palindromy:', sorted(set(wyszukiwaniePalindromow(linie, args))))
        if args.funkcja == '2':
            print('Znalezione palindromy:', wyszukiwaniePalindromow_2(linie, args))
    po = time.perf_counter()
    if args.czas == 'tak':
        print(f"Znaleziono w {po - przed:0.4f} sekund")


if __name__ == "__main__":
    main(parseArguments())







