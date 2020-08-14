# Leia uma temperatura em °C, calcule e escreva a equivalente em °F
# t°F = (9 * t°C + 160) / 5

# Entrada
temp_c = int(input('Digite a temperatura em °C: '))

# Processamento
temp_f = (9 * temp_c + 160) / 5
temp_f = round(temp_f, 2)

# Saída
print(f'{temp_c} °C é equivalente a {temp_f} °F')
