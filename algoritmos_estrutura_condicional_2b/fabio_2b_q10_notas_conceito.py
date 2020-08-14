def main():
    a = float(input('Primeira nota: '))
    b = float(input('Segunda nota: '))

    print('>>> NOTAS: {} e {}'.format(a, b))
    print('>>> MÉDIA: {}'.format(media(a, b)))
    print('>>> CONCEITO: {}'.format(conceito(a, b)))
    print('>>> VOCÊ FOI {}'.format(mensagem(a, b)))


def media(a, b):
    return (a + b) / 2


def conceito(a, b):
    if media(a, b) >= 9 and media(a, b) <= 10:
        return 'A'
    elif media(a, b) < 9 and media(a, b) >= 7.5:
        return 'B'
    elif media(a, b) < 7.5 and media(a, b) >= 6:
        return 'C'
    elif media(a, b) < 6 and media(a, b) >= 4:
        return 'D'
    else:
        return 'E'


def mensagem(a, b):
    if conceito(a, b) == 'A' or conceito(a, b) == 'B' or conceito(a, b) == 'C':
        return 'APROVADO'
    else:
        return 'REPROVADO'


main()