def main():
    palavra = input('Digite a palavra: ')
    right_justificy(palavra)

def right_justificy(s):
    tam_palavra = len(s)
    qtd_espacos = 70 - tam_palavra
    espacos = qtd_espacos * ' '
    linha = espacos + s

    print(linha)

main()