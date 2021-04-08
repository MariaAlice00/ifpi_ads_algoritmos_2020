def duplas_consecutivas():
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip() # strip serve para 'limpar' a palavra
        pos = len(palavra) - 1
        ultima_letra = palavra[pos]
        penultima_letra = palavra[pos - 1]
        for letra in palavra:
            if ord(ultima_letra) == ord(penultima_letra):
                return palavra
            penultima_letra = ultima_letra

    arquivo.close()


def main():
    print(duplas_consecutivas())

main()