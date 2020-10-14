'''Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.'''

def main():
    n = int(input('Número de elementos do vetor: '))
    lista = []
    for a in range(n):
        num = int(input('>>> '))
        lista.append(num)

    print('Existem elementos iguais?')
    resposta = igual(lista)
    print(resposta)


def igual(lista):
    for p in range(len(lista)-1):
        for s in range(p+1, len(lista)):
            if lista[p] == lista[s]:
                return True
    
    return False


if __name__ == "__main__":
    main()