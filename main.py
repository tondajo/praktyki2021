import time
import argparse
import os.path

linie = []
palindromy = []
palindromy1 = []

wyświetlanie = ""
czas = ""
funkcja = ""


parser = argparse.ArgumentParser(description='Wyszukiwanie palindromów')
parser.add_argument('--wyświetlanie', '-w', type=str, help='Umożliwia wyświetlanie wyszukanych palindromów: tak/nie ')
parser.add_argument('--czas', '-c', type=str, help='Umożliwia wyświetlanie czasu wykonania programu: tak/nie', )
parser.add_argument('--funkcja', '-f', type=str, help='Wybiera w jaki sposób zostanie wykonany program: 1/2', )
parser.add_argument('--plik', '-p', type=str, help='Wybiera plik ze słownikiem: (ścieżka do pliku)', )
args = parser.parse_args()

def palindrom1(linie):
    with open('dic\slowa.txt', "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        for slowo in linie:
            if slowo != "":
                if slowo == slowo[::-1]:
                    palindromy1.append(slowo)
    return palindromy1

def reverse(slowo):
    odwroconeSlowo = ''
    for litera in slowo:
        odwroconeSlowo = litera + odwroconeSlowo
    return odwroconeSlowo


def palindrom(linie):
    with open('dic\slowa.txt', "r", encoding="utf-8") as plik:
        linie = [linie[:-(linie[-1] == '\n') or len(linie) + 1] for linie in plik]
        for slowo in linie:
            if reverse(slowo) == slowo:
                palindromy.append(slowo)
    return palindromy


def main():
    przed = time.perf_counter()

    if args.funkcja == '1':
        print('W słowniku znajduje się ', len(palindromy1), 'palindromów.')
        if args.wyświetlanie == 'tak':
            print('Znalezione palindromy:', palindrom1(linie))
    if args.funkcja == '2':
        print('W słowniku znajduje się ', len(palindromy), 'palindromów.')
        if args.wyświetlanie == 'tak':
            print('Znalezione palindromy:', palindrom(linie))
    po = time.perf_counter()
    if args.czas == 'tak':
        print(f"Znaleziono w {po - przed:0.4f} sekund")



if __name__ == "__main__":
    main()







