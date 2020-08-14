def main():
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))

    condicoes(a, b)


def condicoes(a, b):
    if a % b == 1:
        print((a + b) + (a % b))
    elif a % b == 2:
        if a % 2 == 0 and b % 2 != 0:
            print(f'{a} é par e {b} é ímpar')
        elif a % 2 != 0 and b % 2 == 0:
            print(f'{a} é ímpar e {b} é par')
        elif a % 2 == 0 and b % 2 == 0:
            print(f'{a} e {b} são pares')
        else:
            print(f'{a} e {b} são ímpares')
    elif a % b == 3:
        print((a + b) * a)
    elif a % b == 4:
        print((a + b) / b)
    else:
        print(a ** 2) 
        print(b ** 2)


main()