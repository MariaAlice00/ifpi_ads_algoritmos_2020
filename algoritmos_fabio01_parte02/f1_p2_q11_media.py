# Leia 3 números, calcule e escreva a média dos números.

num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro: '))
num_3 = float(input('Digite mais um : '))

media = (num_1 + num_2 + num_3) / 3
media = round(media, 2)

print('A média é: ', media)
