'''Leia uma matriz quadrada de ordem N, calcule e escreva a soma dos elementos da diagonal principal, a soma dos elementos da diagonal secundária e a soma dos elementos que não estão na diagonal principal nem na diagonal secundária'''

def main():
    n = int(input('Ordem da matriz: '))

    matriz = gerar_matriz(n)
    for linha in matriz:
        print(linha)
    
    soma_dp, dp = diagonal_principal(matriz, n)
    print('DIAGONAL PRINCIPAL')
    print('Elementos: {}'.format(dp))
    print('Soma: {}'.format(soma_dp))

    soma_ds, ds = diagonal_secundaria(matriz, n)
    print('DIAGONAL SECUNDÁRIA')
    print('Elementos: {}'.format(ds))
    print('Soma: {}'.format(soma_ds))

    r, soma_resto = resto(matriz, n)
    print('RESTO')
    print('Elementos: {}'.format(r))
    print('Soma: {}'.format(soma_resto))



def gerar_matriz(n):
    matriz = []
    for l in range(n):
        linha = []
        for c in range(n):
            num = int(input('>>> '))
            linha.append(num)
        
        matriz.append(linha)

    return matriz


def diagonal_principal(matriz, n):
    soma_dp = 0
    dp = []
    for c in range(n):
        x = matriz[c][c]
        soma_dp += x
        dp.append(x)

    return soma_dp, dp


def diagonal_secundaria(matriz, n):
    numeros = []
    for l in range(n):
        for c in range(n):
            numeros.append(matriz[l][c])

    soma_ds = 0
    ds = []
    for c in range(n-1, len(numeros)-1, n-1):
        x = numeros[c]
        soma_ds += x
        ds.append(x)

    return soma_ds, ds


def resto(matriz, n):
    soma_dp, dp = diagonal_principal(matriz, n)
    soma_ds, ds = diagonal_secundaria(matriz, n)

    numeros = []
    for l in range(n):
        for c in range(n):
            numeros.append(matriz[l][c])

    s = dp + ds

    i = 0
    for i in numeros[:]:
        if i in s:
            numeros.remove(i) 

    soma_resto = 0
    for num in numeros:
        soma_resto += num

    return numeros, soma_resto


if __name__ == "__main__":
    main()