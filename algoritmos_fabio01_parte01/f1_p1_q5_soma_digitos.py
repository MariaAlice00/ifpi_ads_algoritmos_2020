# Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U)

# Entrada
num = int(input('Digite um número de três dígitos:'))

# Processamento
C = num // 1 % 10
D = num // 10 % 10
U = num // 100 % 10
soma = C + D + U

# Saída
print('A soma dos dígitos é: {}'.format(soma))
