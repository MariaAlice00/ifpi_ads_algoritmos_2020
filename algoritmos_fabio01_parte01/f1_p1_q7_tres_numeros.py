# Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

# Entrada
num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))
num_3 = int(input('Digite um número: '))

# Processamento
soma = num_1 + num_2
diferença = num_2 - num_3

# Saída
print('A soma de {} e {} é {}'.format(num_1, num_2, soma))
print('A diferença de {} com {} é {}'.format(num_2, num_3, diferença))
