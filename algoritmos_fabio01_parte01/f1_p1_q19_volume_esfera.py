# Leia o valor do raio de uma esfera, calcule e escreva seu volume.
# v = (4 * p * r ** 3) / 3

# Entrada
p = 3.14
r = int(input('Digite o valor do raio: '))

# Processamento
volume = (4 * p * r ** 3) / 3
volume = round(volume, 2)

# Saída
print('O volume é: ', volume)
