def ordem_crescente(a, b, c):
    if a < b < c:
        print(f'{a} < {b} < {c}')
    elif a < c < b:
        print(f'{a} < {c} < {b}')
    elif b < a < c:
        print(f'{b} < {a} < {c}')
    elif b < c < a:
        print(f'{b} < {c} < {a}')
    elif c < a < b:
        print(f'{c} < {a} < {b}')
    else:
        print(f'{c} < {b} < {a}')


def main():
    a = int(input('Digite um 1º número: '))
    b = int(input('Digite um 2º número: '))
    c = int(input('Digite um 3º número: '))

    ordem_crescente(a, b, c)


main()