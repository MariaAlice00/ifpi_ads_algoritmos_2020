def triangulo_lados(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print('Forma um triângulo equilátero.')
        elif a == b != c or a == c != b or b == c != a:
            print('Forma um triângulo isósceles.')
        else:
            print('Forma um triângulo escaleno.')
    else:
        print('Não forma um triângulo.')


def main():
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    c = int(input('Terceiro valor: '))
    
    triangulo_lados(a, b, c)

    
main()