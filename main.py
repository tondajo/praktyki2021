import time
import argparse

linie = []
palindromy = []

wyświetlanie = ""
czas = ""

parser = argparse.ArgumentParser(description='Wyszukiwanie palindromów')
parser.add_argument('--wyświetlanie', '-w', type=str, help='Umożliwia wyświetlanie wyszukanych palindromów', )
parser.add_argument('--czas', '-c', type=str, help='Umożliwia wyświetlanie czasu wykonania programu', )
parser.add_argument('--funkcja', '-f', type=str, help='Wybiera w jaki sposób zostanie wykonany program', )
parser.add_argument('--plik', '-p', type=str, help='Wybiera plik ze słownikiem', )
args = parser.parse_args()

print(args.czas)



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
    if args.wyświetlanie == 'tak':
        print('Znalezione palindromy:', palindrom(linie))
    print('W słowniku znajduje się ', len(palindromy), 'palindromów.')
    po = time.perf_counter()
    if args.czas == 'tak':
        print(f"Znaleziono w {po - przed:0.4f} sekund")



if __name__ == "__main__":
    main()







