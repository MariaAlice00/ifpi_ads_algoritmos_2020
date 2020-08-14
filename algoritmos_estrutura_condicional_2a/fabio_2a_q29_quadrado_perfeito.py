def main():
    num = int(input('Digite um número de 4 dígitos: '))

    print('{} {}'.format(num, quadrado(num)))


def quadrado(num):
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    num1 = m * 10 + c
    num2 = d * 10 + u

    num3 = num1 + num2

    if num3 ** 2 == num:
        return 'é um quadrado perfeito'
    else:
        return 'não é um quadrado perfeito'


main()