# Leia um número inteiro (3 dígitos) e escreva o inverso do número.

# Entrada
num = int(input('Digite um número: '))

# Processamento
num_1 = num // 1 % 10
num_2 = num // 10 % 10
num_3 = num // 100 % 10

# Saída
print(f'O inverso de {num} é {num_1}{num_2}{num_3}')
