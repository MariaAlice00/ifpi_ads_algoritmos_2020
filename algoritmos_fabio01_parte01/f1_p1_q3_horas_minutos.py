# Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos

# Entrada
valor_m = int(input('Valor em minutos: '))

# Processamento
h = valor_m // 60
m = valor_m % 60

# Saída
print(f'{valor_m} minutos é igual a {h} horas e {m} minutos')
