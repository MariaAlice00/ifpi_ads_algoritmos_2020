def main():
    a = int(input('Lado 1: '))
    b = int(input('Lado 2: '))
    c = int(input('Lado 3: '))
    
    hipotenusa_catetos(a, b, c)


def hipotenusa_catetos(a, b, c):
    if a > b and a > c and a < b + c:
        print(f'{a} é a hipotenusa; {b} e {c} são os catetos.')
    elif b > a and b > c and b < a + c:
        print(f'{b} é a hipotenusa; {a} e {c} são os catetos.')
    else:
        print(f'{c} é a hipotenusa; {a} e {b} são os catetos.')


main()