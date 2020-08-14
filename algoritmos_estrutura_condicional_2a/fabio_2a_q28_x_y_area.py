def main():
    x1 = int(input('X1: '))
    y1 = int(input('Y1: '))
    x2 = int(input('X2: '))
    y2 = int(input('Y2: '))

    print('ÁREA: {}'.format(area(x1, x2, y1, y2)))


def base(x1, x2):
    base = x1 - x2
    if base < 0:
        return abs(base)
    else:
        return base   


def altura(y1, y2):
    altura = y1 - y2
    if altura < 0:
        return abs(altura)
    else:
        return altura


def area(x1, x2, y1, y2):
    return base(x1, x2) * altura(y1, y2)


main()
