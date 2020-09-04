# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

def main():
    num = int(input('>>> '))

    a = 0
    b = 1
    print('{} -> {}'.format(a, b), end='')

    for c in range(2, num):
        c = a + b
        a = b
        b = c

        print(' -> {}'.format(c), end='')


main()