# Leia o valor da base e altura de um retângulo, calcule e escreva sua área.
# área = base * altura

# Entrada
base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

# Processamento
area = base * altura
area = round(area, 2)

# Saída
print('A área é igual a: ', area)
