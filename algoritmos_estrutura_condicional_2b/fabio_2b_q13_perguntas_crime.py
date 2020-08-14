def main():
    print('Vou fazer 5 perguntas. Responda sim ou não.')
    a = str(input('Telefonou para a vítima? '))
    b = str(input('Esteve no local do crime? '))
    c = str(input('Mora perto da vítima? '))
    d = str(input('Devia para a vítima? '))
    e = str(input('Já trabalhou com a vítima? '))

    print('Você é: {}'.format(resultado(a, b, c, d, e)))


def pergunta_a(a):
    if a == 'sim':
        return 1
    elif a == 'não':
        return 0


def pergunta_b(b):
    if b == 'sim':
        return 1
    elif b == 'não':
        return 0


def pergunta_c(c):
    if c == 'sim':
        return 1
    elif c == 'não':
        return 0


def pergunta_d(d):
    if d == 'sim':
        return 1
    elif d == 'não':
        return 0


def pergunta_e(e):
    if e == 'sim':
        return 1
    elif e == 'não':
        return 0


def perguntas_total(a, b, c, d, e):
    return pergunta_a(a) + pergunta_b(b) + pergunta_c(c) + pergunta_d(d) + pergunta_e(e)


def resultado(a, b, c, d, e):
    if perguntas_total(a, b, c, d, e) == 2:
        return 'SUSPEITO'
    elif perguntas_total(a, b, c, d, e) == 3 or perguntas_total(a, b, c, d, e) == 4:
        return 'CÚMPLICE'
    elif perguntas_total(a, b, c, d, e) == 5:
        return 'ASSASSINO'
    else:
        return 'INOCENTE'


main()