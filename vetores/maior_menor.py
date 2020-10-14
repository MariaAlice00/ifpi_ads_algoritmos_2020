'''Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas posições no vetor.'''

def main():
    n = int(input('Número de elementos: '))

    vetor = []
    for c in range(n):
        num = int(input('>>> '))
        vetor.append(num)

    print(vetor)
    maior = maior_elemento(vetor)
    menor = menor_elemento(vetor)
    print('Maior elemento: {}'.format(maior))
    print('Menor elemento: {}'.format(menor))


def maior_elemento(vetor):
    maior = 0
    for num in vetor:
        if num > maior:
            maior = num
    
    return maior


def menor_elemento(vetor):
    maior = maior_elemento(vetor)
    menor = maior
    for num in vetor:
        if num < menor:
            menor = num

    return menor


if __name__ == "__main__":
    main()