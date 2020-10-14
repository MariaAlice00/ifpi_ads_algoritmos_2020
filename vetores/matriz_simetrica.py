'''Leia uma matriz quadrada de ordem N e escreva se ela é ou não simétrica. Uma matriz quadrada é dita simétrica se A[i,j] =A[j,i].'''

def main():
    n = int(input('Ordem da matriz: '))

    matriz = gerar_matriz(n)
    for linha in matriz:
        print(linha)
    
    resposta = avaliar(matriz, n)
    print('É simétrica? {}'.format(resposta))
    

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
    dp = []
    for c in range(n):
        x = matriz[c][c]
        dp.append(x)

    return dp


def todos_numeros(matriz, n):
    tn = []
    for l in range(n):
        for c in range(n):
            tn.append(matriz[l][c])

    return tn


def resto(matriz, n):
    resto_numeros = []
    for l in range(n):
        for c in range(n-1, -1, -1):
            if l != c:
                if matriz[l][c] == matriz[c][l]:
                    resto_numeros.append(matriz[l][c])

    return resto_numeros


def avaliar(matriz, n):
    tn = todos_numeros(matriz, n)
    numeros = resto(matriz, n)
    dp = diagonal_principal(matriz, n)

    s = numeros + dp
    s.sort()
    tn.sort()

    if tn == s:
        return True
    else:
        return False


if __name__ == "__main__":
    main()