def main():
    N = int(input('>>> '))

    n = 1
    d = N
    soma = 0

    while n <= N:
        y = n / d
        soma += y

        n += 1
        d -= 1

    print(soma)

main()
