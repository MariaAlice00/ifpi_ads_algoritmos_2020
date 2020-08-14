def main():
    a = int(input('Digite o 1º número: '))
    b = int(input('Digite o 2º número: '))
    c = int(input('Digite o 3º número: '))
    d = int(input('Digite o 4º número: '))
    e = int(input('Digite o 5º número: '))

    media_tela(a, b, c, d, e)


def media_tela(a, b, c, d, e):
    media = (a + b + c + d + e) / 5
    print('Os números que são maiores que a média são: ')
    se_maior(a, media)
    se_maior(b, media)
    se_maior(c, media)
    se_maior(d, media)
    se_maior(e, media)


def se_maior(num_def, num_qual):
    if num_def > num_qual:
        print(num_def, end=' ')


main()