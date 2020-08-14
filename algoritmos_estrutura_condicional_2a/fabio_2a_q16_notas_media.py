def main():
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))

    media(nota1, nota2)


def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        print('APROVADO!!!')
    else:
        media_final(media)


def media_final(media):
    nota_exame = float(input('Nota do exame: '))
    media_final = (media + nota_exame) / 2
    if media_final >= 5:
        print('APROVADO!')
    else:
        print('REPROVADO.')


main()