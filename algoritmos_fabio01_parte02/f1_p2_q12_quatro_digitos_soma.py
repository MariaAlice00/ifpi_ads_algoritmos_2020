# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem.
# Ex:número = 9534 ; soma = 9+5+3+4 = 21.

num = int(input('Digite um número de quatro dígitos: '))

num_1 = num // 1 % 10
num_2 = num // 10 % 10
num_3 = num // 100 % 10
num_4 = num // 1000 % 10
soma = num_1 + num_2 + num_3 + num_4 

print('O resultado é: ', soma)
