# Leia N e escreva todos os números inteiros pares de 1 a N.

def main():
    n = int(input('>>> '))
    x = 1
    while x <= n:
        if x % 2 == 0:
            print(x)
        x += 1
    print('Fim...')

main()
