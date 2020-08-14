# Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

# Entrada
num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite um número: '))

# Processamento
soma = num_1 + num_2
diferenca = num_1 - num_2
divisao = soma / diferenca

# Saída
print('RESULTADO = {:.2f}'.format(divisao))
