# Leia o valor do lado de um quadrado, calcule e escreva sua área.
# Área = lado ** 2

# Entrada
lado = float(input('Digite o valor do lado: '))

#Processamento
area = lado ** 2
area = round(area, 2)

# Saída
print(f'A área de lado {lado} é igual a {area}')
