# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

from random import randint
n = int(input('>>> '))
contador = 1
soma = 0

while True:
    num = randint(0,10)
    contador = contador + 1
    if contador > n + 1:
        break

    print(num, end=' ')
    soma = soma + num

print('\nSoma = {}'.format(soma))
print('Média = {}'.format(soma / n))
