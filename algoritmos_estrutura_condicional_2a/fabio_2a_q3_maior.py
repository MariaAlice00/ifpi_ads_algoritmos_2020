def maior(a, b, c):
    if a > b and a > c:
        print(f'O maior número é {a}.')
    elif b > a and b > c:
        print(f'O maior número é {b}.')
    else:
        print(f'O maior número é {c}.')


def main():
    a = int(input('Digite um 1º número: '))
    b = int(input('Digite um 2º número: '))
    c = int(input('Digite um 3º número: '))

    maior(a, b, c)


main()
