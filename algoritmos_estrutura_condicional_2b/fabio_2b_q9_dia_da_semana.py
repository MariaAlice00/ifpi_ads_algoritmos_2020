def main():
    num = int(input('Digite um número inteiro: '))

    print(num_semana(num))


def num_semana(num):
    if num == 1:
        return 'DOMINGO'
    elif num == 2:
        return 'SEGUNDA'
    elif num == 3:
        return 'TERÇA'
    elif num == 4:
        return 'QUARTA'
    elif num == 5:
        return 'QUINTA'
    elif num == 6:
        return 'SEXTA'
    elif num == 7:
        return 'SÁBADO'
    else:
        return 'VALOR INVÁLIDO'


main()