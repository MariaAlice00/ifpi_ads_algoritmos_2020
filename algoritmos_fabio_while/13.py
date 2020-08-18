# Leia N e uma lista de N números e escreva o maior número da lista.
from random import randint

n = int(input('>>> '))
contador = 1
lista = []

while True:
    num = randint(0,10)
    contador = contador + 1
    if contador > n + 1:
        break
    
    lista.append(num) # append: adiciona um item na lista
    print(num, end=' ')

print('\nMaior número: {}'.format(max(lista)))
