def main():
    letra = str(input('Digite uma letra maiúscula: '))

    print(genero(letra))


def genero(letra):
    if letra == 'F':
        return 'FEMININO'
    elif letra == 'M':
        return 'MASCULINO'
    else:
        return 'SEXO INVÁLIDO'


main()