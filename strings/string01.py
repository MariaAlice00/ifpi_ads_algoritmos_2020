def main():
    texto = input('Texto: ')
    letra = input('Letra: ')

    contador = 0

    for c in texto: # para cada caractere em texto
        if c == letra:
            contador += 1
    print(f'O caractere "{letra}" aparece {contador}x')

main()