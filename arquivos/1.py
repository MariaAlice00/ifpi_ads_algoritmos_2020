def main():
    frutas = []

    arquivo = open('frutas.txt', 'r')

    for fruta in arquivo:
        linha = f'{fruta}\n'
        frutas.append(linha.strip())

    arquivo.close()

    print(frutas)

main()