def main():
    n = 1
    d = 1
    soma = 0

    while n <= 99 and d <= 50:
        y = n / d
        soma += y

        n += 2
        d += 1

    print('Soma = {}'.format(soma))

main()
