'''Leia N e uma lista de N números e escreva o maior número da lista.'''

def main():
    from random import randint

    n = int(input('>>> '))
    contador = 1
    lista = []

    for c in range(1, n+1):
        num = randint(0,10)
        contador = contador + 1

        lista.append(num)
        print(num, end=' ')

    print('\nMaior número: {}'.format(max(lista)))

main()