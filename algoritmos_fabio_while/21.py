def main():
    n = 1
    d = 1
    s = 0

    while n <= 99 and d <= 50:
        y = n / d
        s += y

        n += 2
        d += 1

    print('S = {}'.format(s))

main()
