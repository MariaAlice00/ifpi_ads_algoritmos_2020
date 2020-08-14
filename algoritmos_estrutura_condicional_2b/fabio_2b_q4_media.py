def main():
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media(nota1, nota2)


def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media == 10:
        print('APROVADO COM DISTINÇÃO!!!')
    elif media >= 7:
        print('APROVADO!')
    else:
        print('REPROVADO.')


main()