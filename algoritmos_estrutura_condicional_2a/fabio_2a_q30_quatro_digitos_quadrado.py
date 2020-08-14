def main():
    num = int(input('Digite um número de 4 digítos: '))
    print('O número que você digitou: {}'.format(num))
    print('O número que resultou: {}'.format(separar(num)))


def separar(num):
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    num1 = m * 10 + c
    num2 = d * 10 + u

    num3 = num1 + num2

    num4 = num3 ** 2

    if num4 == num:
        return num4
    else:
        return num4


main()