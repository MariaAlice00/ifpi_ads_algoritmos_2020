def main():
    a = int(input('Digite o 1º número: '))
    b = int(input('Digite o 2º número: '))
    c = int(input('Digite o 3º número: '))
    d = int(input('Digite o 4º número: '))
    e = int(input('Digite o 5º número: '))

    maior(a, b, c, d, e)
    menor(a, b, c, d, e)


def maior(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        print(f'{a} é maior')
    elif b > a and b > c and b > d and b > e:
        print(f'{b} é maior')
    elif c > a and c > b and c > d and c > e:
        print(f'{c} é maior')
    elif d > a and d > b and d > c and d > e:
        print(f'{d} é maior')
    else:
        print(f'{e} é maior')


def menor(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        print(f'{a} é menor')
    elif b < a and b < c and b < d and b < e:
        print(f'{b} é menor')
    elif c < a and c < b and c < d and c < e:
        print(f'{c} é menor')
    elif d < a and d < b and d < c and d < e:
        print(f'{d} é menor')
    else:
        print(f'{e} é menor')


main()