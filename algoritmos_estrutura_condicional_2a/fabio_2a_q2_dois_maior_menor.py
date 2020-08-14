def maior_menor(a, b):
    if a > b:
        print(f'O maior é {a} e o menor é {b}.')
    else:
        print(f'O maior é {b} e o menor é {a}.')


def main():
    a = int(input('Digite 1º número inteiro: '))
    b = int(input('Digite 2º número inteiro: '))
    
    maior_menor(a, b)


main()