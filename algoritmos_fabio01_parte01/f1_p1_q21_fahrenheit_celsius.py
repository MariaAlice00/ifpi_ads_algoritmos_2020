# Leia uma temperatura em °F, calcule e escreva a equivalente em °C.
# t°C = (5 * t°F - 160) / 9

# Entrada
temp_f = int(input('Digite a temperatura em °F: '))

# Processamento
temp_c = (5 * temp_f - 160) / 9
temp_c = round(temp_c, 2)

# Saída
print(f'{temp_f} °F equivale a {temp_c} °C')

