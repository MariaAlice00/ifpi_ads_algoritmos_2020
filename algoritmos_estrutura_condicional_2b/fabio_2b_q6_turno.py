def main():
    letra = str(input('Digite uma letra maiúscula: '))

    print(turno(letra))


def turno(letra):
    if letra == 'M':
        return 'BOM DIA!'
    elif letra == 'V':
        return 'BOA TARDE!'
    elif letra == 'N':
        return 'BOA NOITE!'
    else:
        return 'VALOR INVÁLIDO!'


main()