'''Leia N e escreva todos os números inteiros pares de 1 a N.'''

def main():
    n = int(input('>>> '))

    for c in range(1, n+1):
        if c % 2 == 0:
            print(c)


main()