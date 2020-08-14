def main():
    letra = str(input('Digite uma letra: '))

    print(vogal_consoante(letra))


def vogal_consoante(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return 'É UMA VOGAL'
    else:
        return 'É UMA CONSOANTE'


main()