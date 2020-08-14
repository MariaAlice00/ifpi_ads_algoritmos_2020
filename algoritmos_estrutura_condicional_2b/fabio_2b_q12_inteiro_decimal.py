def main():
    num = float(input('Digite um número: '))
    print('{} {}'.format(num, inteiro_decimal(num)))


def inteiro_decimal(num):
    if num // 1 == num:
        return 'é um número inteiro.'
    else:
        return 'é um número decimal.'


main()