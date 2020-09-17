def main():
    num = int(input())
    password = input()

    print(strong_password(password))


def strong_password(password):
    d, ma, mi, ce = verificar(password)
    cont = 0

    if d == 0:
        cont += 1    
    if ma == 0:
        cont += 1
    if mi == 0:
        cont += 1
    if ce == 0:
        cont += 1
    if (d + ma + mi + ce +cont) < 6:
        cont = cont + (6 - (d + ma + mi + ce + cont))

    return cont


def verificar(password):
    d = 0
    ma = 0
    mi = 0
    ce = 0

    for pos in password:
        if digito(pos):
            d += 1
        elif eh_letra_maiuscula(pos):
            ma += 1
        elif eh_letra_minuscula(pos):
            mi += 1
        elif caract_especial(pos):
            ce += 1

    return d, ma, mi, ce


def digito(pos):
    return ord(pos) >= 48 and ord(pos) <= 57


def eh_letra_maiuscula(pos):
    return ord(pos) >= 65 and ord(pos) <= 90


def eh_letra_minuscula(pos):
    return ord(pos) >= 97 and ord(pos) <= 122


def caract_especial(pos):
    return ord(pos) == 33 or ord(pos) == 35 or ord(pos) == 36 or ord(pos) == 37 or ord(pos) == 38 or ord(pos) == 40 or ord(pos) == 41 or ord(pos) == 42 or ord(pos) == 43 or ord(pos) == 45 or ord(pos) == 64 or ord(pos) == 94


main()