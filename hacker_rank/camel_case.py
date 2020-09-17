def main():
    s = str(input())

    num_palavras = analisando(s)
    print(num_palavras)


def analisando(s):
    tam_s = len(s)
    contador = 1

    for c in range(0, tam_s):
        pos = s[c]
        if eh_letra_maiuscula(pos):
            contador += 1
        elif eh_letra_minuscula(pos):
            contador += 0

    return contador            


def eh_letra_maiuscula(pos):
    return ord(pos) >= 65 and ord(pos) <= 90


def eh_letra_minuscula(pos):
    return ord(pos) >= 97 and ord(pos) <= 122


main()
