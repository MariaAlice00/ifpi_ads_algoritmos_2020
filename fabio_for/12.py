'''Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.'''

def main():
    from random import randint

    n = int(input('>>> '))
    contador = 1
    soma = 0
    for c in range(1, n+1):
        num = randint(0, 10)
        print(num, end=' ')

        soma = soma + num

    print('\nSoma = {}'.format(soma))
    print('Média = {}'.format(soma / n))

main()