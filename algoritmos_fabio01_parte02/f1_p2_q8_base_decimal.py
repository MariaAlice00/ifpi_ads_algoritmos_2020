# Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

num = int(input('Digite um número binário de 4 dígitos: '))

num_1 = num // 1000 % 10
num_2 = num // 100 % 10
num_3 = num // 10 % 10
num_4 = num // 1 % 10

bin_1 = num_1 * 2 ** 3
bin_2 = num_2 * 2 ** 2
bin_3 = num_3 * 2 ** 1
bin_4 = num_2 * 2 ** 0
bin_final = bin_1 + bin_2 + bin_3 + bin_4

print('O número binário {} equivale a {} na base decimal'.format(num, bin_final))

