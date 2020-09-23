def main():
    menu = '##### WordPlay #####\n' \
    + '1 - Palavras com mais de 20 letras\n' \
    + '2 - Palavras sem "e"\n' \
    + '3 - Palavras sem as letras proibidas\n' \
    + '4 - Palavras com uma série de letras\n' \
    + '5 - Palavras com letras obrigatórias\n' \
    + '6 - Palavras em que as letras estão em ordem alfabética\n' \
    + '0 - Sair\n' \
    + 'Digite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_mais_20()
        elif opcao == 2:
            palavras_sem_letra_e()
        elif opcao == 3:
            letras_proibidas = input('Digite as letras proibidas: ')
            palavras_sem_letras_proibidas(letras_proibidas)
        elif opcao == 4:
            serie_letras = input('Com quais letras você quer formar as palavras? ')
            palavras_serie_letras(serie_letras)
        elif opcao == 5:
            letras_obrigatorias = input('Digite as letras obrigatórias: ')
            palavras_letras_obrigatorias(letras_obrigatorias)
        elif opcao == 6:
            palavras_ordem_alfabetica()
        else:
            print('Opção inválida!')

        input('Continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim')


def palavras_mais_20():
    print('>>> Palavras com mais de 20 letras <<<')
    
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip() # strip serve para 'limpar' a palavra
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>>> Palavras sem a letra "e" <<<')

    arquivo = open('words.txt')
    total_palavras = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total_palavras += 1
        if has_no_e(palavra):
            palavras_sem_e += 1 
            print(palavra)

    percentual = (palavras_sem_e / total_palavras) * 100
    print('Total de palavras: {}'.format(total_palavras))
    print('Palavras sem "e": {}'.format(palavras_sem_e))
    print('Percentual: {}%'.format(percentual))

    arquivo.close()


def has_no_e(palavra):
    #return 'e' not in palavra
    for letra in palavra:
        if letra == 'e':
            return False
    
    return True


def palavras_sem_letras_proibidas(letras_proibidas):
    c = 0
    print('>>> Palavras sem as letras proibidas <<<')

    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras_proibidas):
            c += 1
            print(palavra)
    
    print('Total de palavras sem as letras proibidas: {}'.format(c))


def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if letra in letras_proibidas:
            return False
    return True


def palavras_serie_letras(serie_letras):
    i = 0
    print('>>> Palavras com a série de letras <<<')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if uses_only(palavra, serie_letras):
            i += 1
            print(palavra)
    
    print('Total de palavras com a série de letras: {}'.format(i))


def uses_only(palavra, serie_letras):
    for letra in palavra:
        if letra not in serie_letras:
            return False
    return True


def palavras_letras_obrigatorias(letras_obrigatorias):
    t = 0
    print('>>> Palavras com as letras obrigatórias <<<')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if uses_all(palavra, letras_obrigatorias):
            t += 1
            print(palavra)
    
    print('Total de palavras com as letras obrigatórias: {}'.format(t))


def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if letra not in palavra:
            return False
    return True


def palavras_ordem_alfabetica():
    w = 0
    print('>>> Palavras em que as letras estão em ordem alfabética <<<')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if is_abecedarian(palavra):
            w += 1
            print(palavra)
    
    print('Total de palavras em que as letras estão em ordem alfabética: {}'.format(w))


def is_abecedarian(palavra):
    palavra_anterior = palavra[0]
    for letra in palavra:
        if ord(letra) < ord(palavra_anterior):
            return False
        palavra_anterior = letra
    return True


main()