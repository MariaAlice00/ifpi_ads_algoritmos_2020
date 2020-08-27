def main():
    N = int(input('>>> '))

    n = 1
    d = N
    s = 0

    while n <= N:
        y = n / d
        s += y

        n += 1
        d -= 1

    print('S = {}'.format(s))


main()
