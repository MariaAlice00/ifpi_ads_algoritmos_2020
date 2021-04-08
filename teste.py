'''Leia uma matriz quadrada de ordem N e encontre a linha que possui a maior e a menor soma dos elementos.'''

def main():
    n = int(input('Ordem da matriz: '))

    matriz = gerar_matriz(n)
    
    for linha in matriz:
        print(linha)


    lma, maior = maior_linha(linha, matriz)
    print('Maior: Linha {} -> {}'.format(lma, maior))

    lme, menor = menor_linha(linha, matriz)
    print('Menor: Linha {} -> {}'.format(lme, menor))
    

def gerar_matriz(n):
    matriz = []
    for l in range(n):
        linha = []
        for c in range(n):
            num = int(input('>>> '))
            linha.append(num)
        
        matriz.append(linha)

    return matriz



def linhas(matriz, n):
    for c in range(n):
        linha = matriz[c]

    return linha


def soma_linha(linha):
    s = 0
    for num in linha:
        s += num
    
    return s


def todas_somas(linha, matriz):
    somas = []
    c = 0
    for linha in matriz:
        s = soma_linha(linha)
        somas.append(s)
        c += 1

    return somas


def maior_linha(linha, matriz):
    somas = todas_somas(linha, matriz)
    i = 0
    maior = 0
    for num in somas:
        if num > maior:
            maior = num
            lma = i
        i += 1

    return lma, maior


def menor_linha(linha, matriz):
    somas = todas_somas(linha, matriz)
    lma, maior = maior_linha(linha, matriz)
    i = 0
    menor = maior
    for num in somas:
        if num < menor:
            menor = num
            lme = i
        i += 1

    return lme, menor


if __name__ == "__main__":
    main()