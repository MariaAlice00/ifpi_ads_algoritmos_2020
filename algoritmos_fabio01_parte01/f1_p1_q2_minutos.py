# Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

# Entrada
horas = int(input('Valor em horas: '))
minutos = int(input('Valor em minutos: '))

# Processamento
total_minutos = (horas * 60) + minutos

# Saída
print('A soma de {} horas com {} minutos equivale a {} minutos'.format(horas, minutos,total_minutos))
