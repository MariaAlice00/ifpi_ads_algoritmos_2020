def main():
    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))
    c = float(input('Valor de c: '))

    print(raizes(a, b, c))


def delta(a, b, c):
    return b ** 2 - (4 * a * c)


def raizes(a, b, c):
    if delta(a, b, c) > 0:
        x1 = (-b + delta(a, b, c) ** (1/2)) / 2 * a
        x2 = (-b - delta(a, b, c) ** (1/2)) / 2 * a
        return f'Existem duas raízes reais e distintas: {x1} e {x2}'
    elif delta(a, b, c) == 0:
        x = (-b + delta(a, b, c) ** (1/2)) / 2 * a
        return f'Existem duas raízes reais e com o mesmo valor: {x}'
    else:
        return 'Não existem raízes reais'


main()
