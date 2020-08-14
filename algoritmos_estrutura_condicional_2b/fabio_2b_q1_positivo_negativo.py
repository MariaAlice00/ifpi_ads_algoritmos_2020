def main():
    num = float(input('Digite um número: '))
    positivo_negativo(num)


def positivo_negativo(num):
    if num < 0:
        print(f'{num} é negativo')
    else:
        print(f'{num} é positivo')


main()
