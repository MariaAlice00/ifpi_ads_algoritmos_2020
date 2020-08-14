# Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s
# Vm/s = Vkm/h / 3.6

# Entrada
velocidade_km_h = float(input('Digite uma velocidade em km/h: '))

# Processamento
velocidade_ms = velocidade_km_h / 3.6
velocidade_ms = round(velocidade_ms, 2)

# Saída
print(f'{velocidade_km_h} km/h é equivalente a {velocidade_ms} m/s')
