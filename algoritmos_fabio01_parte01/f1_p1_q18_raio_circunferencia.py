# Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.
# c = 2 * p * r

# Entrada
p = 3.141592
r = float(input('Digite o valor do raio: '))

# Processamento
comprimento = 2 * p * r
comprimento = round(comprimento, 2)

# Saída
print('O comprimento da circuferência é: ', comprimento)
