def main():
    qtd = int(input('Quantos números você quer digitar? '))
    valor_padrao = -1
    numeros = gerar_numeros(qtd, valor_padrao)

    for posicao in range(len(numeros)):
        valor = int(input('Número {}: '.format(posicao)))
        numeros[posicao] = valor

    quantidade_pares = pares(numeros)
    quantidade_impares = impares(numeros)
    quantidade_positivos = positivos(numeros)
    quantidade_negativos = negativos(numeros)

    print(numeros)
    print(f'Pares: {quantidade_pares}')
    print(f'Ímpares: {quantidade_impares}')
    print(f'Positivos: {quantidade_positivos}')
    print(f'Negativos: {quantidade_negativos}')

    novos_numeros = substituir(numeros)
    print('\n***** NOVOS NÚMEROS *****')
    for posicao in range(len(novos_numeros)):
        valor = novos_numeros[posicao]
        print(f'Número {posicao}: {valor}')

    quantidade_nova_pares = pares(novos_numeros)
    quantidade_nova_impares = impares(novos_numeros)
    quantidade_nova_positivos = positivos(novos_numeros)
    quantidade_nova_negativos = negativos(novos_numeros)

    print(novos_numeros)
    print(f'Pares: {quantidade_nova_pares}')
    print(f'Ímpares: {quantidade_nova_impares}')
    print(f'Positivos: {quantidade_nova_positivos}')
    print(f'Negativos: {quantidade_nova_negativos}')

    media = media_numeros_novos(novos_numeros)
    print(f'Média: {media}')


def gerar_numeros(qtd, valor_padrao):
    return [valor_padrao] * qtd


def pares(numeros):
    par = 0
    for item in numeros:
        if item % 2 == 0:
            par += 1

    return par


def impares(numeros):
    impar = 0
    for item in numeros:
        if item % 2 != 0:
            impar += 1

    return impar


def positivos(numeros):
    positivos = 0
    for item in numeros:
        if item > 0:
            positivos += 1
    
    return positivos


def negativos(numeros):
    negativos = 0
    for item in numeros:
        if item < 0:
            negativos += 1

    return negativos


def substituir(numeros):
    for i in range(len(numeros)):
        if i % 2 == 0 :
            numeros[i] = numeros[i] * 2
        else:
            numeros[i] = numeros[i] / 2     

    return numeros           


def media_numeros_novos(novos_numeros):
    soma = 0
    c = 0

    for item in novos_numeros:
        soma += item
        c += 1
    
    return soma/c
    

main()
