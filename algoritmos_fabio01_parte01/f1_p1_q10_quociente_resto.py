# Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1° pelo 2°.

# Entrada
num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite um número inteiro: '))

# Processamento
quociente = num_1 // num_2
resto = num_1 % num_2

# Saída
print('Divisão de {} com {}'.format(num_1, num_2))
print('>>> Quociente = {}'.format(quociente))
print('>>> Resto = {}'.format(resto))
