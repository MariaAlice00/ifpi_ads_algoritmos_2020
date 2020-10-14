'''Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas posições no vetor.'''

def main():
    n = int(input('Número de elementos: '))

    vetor = []
    for c in range(n):
        num = int(input('>>> '))
        vetor.append(num)

    print(vetor)
    maior, pos_maior = maior_elemento(vetor)
    menor, pos_menor = menor_elemento(vetor)
    print('Maior elemento: {} -> Posição {}'.format(maior, pos_maior))
    print('Menor elemento: {} -> Posição {}'.format(menor, pos_menor))


def maior_elemento(vetor):
    maior = 0
    i = 0
    for num in vetor:
        if num > maior:
            maior = num
            pos_maior = i
        i += 1
    
    return maior, pos_maior


def menor_elemento(vetor):
    maior, pos_maior = maior_elemento(vetor)
    menor = maior
    i = 0
    for num in vetor:
        if num < menor:
            menor = num
            pos_menor = i
        i += 1

    return menor, pos_menor


if __name__ == "__main__":
    main()
