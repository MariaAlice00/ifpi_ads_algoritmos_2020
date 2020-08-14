def triangulo_angulos(a, b, c):
    if a + b + c == 180:
        if a < 90 and b < 90 and c < 90:
            print('Forma um triângulo acutângulo.')
        elif a > 90 or b > 90 or c > 90:
            print('Forma um triângulo obtusângulo.')
        else:
            print('Forma um triângulo retângulo.')
    else:
        print('Não irá formar um triângulo.')


def main():
    a = int(input('Digite o 1º ângulo: '))
    b = int(input('Digite o 2º ângulo: '))
    c = int(input('Digite o 3º ângulo: '))

    triangulo_angulos(a, b, c)


main()