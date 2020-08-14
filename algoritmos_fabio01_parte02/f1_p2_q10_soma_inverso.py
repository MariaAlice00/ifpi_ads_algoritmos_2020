# Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# Ex: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

num = int(input('Digite um número de três dígitos: '))

num_1 = num // 1 % 10
num_2 = num // 10 % 10
num_3 = num // 100 % 10
inverso = num_1 * 100 + num_2 * 10 + num_3 * 1
soma = num + inverso

print('A soma entre {} e {} é {}'.format(num, inverso, soma))