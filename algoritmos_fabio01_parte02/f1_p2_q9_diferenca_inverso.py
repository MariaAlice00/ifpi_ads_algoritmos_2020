# Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

num = int(input('Digite um número de três dígitos: '))

num_1 = num // 1 % 10
num_2 = num // 10 % 10
num_3 = num // 100 % 10
inverso = num_1 * 100 + num_2 * 10 + num_3 * 1
diferenca = num - inverso

print('A diferença entre {} e {} é {}'.format(num, inverso, diferenca))
