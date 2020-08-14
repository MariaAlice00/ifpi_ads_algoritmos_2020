# Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

# Entrada
salario = float(input('Digite o salário: '))

# Processamento
aumento = 25 / 100 * salario
salario_com_aumento = aumento + salario
salario_com_aumento = round(salario_com_aumento, 2)

# Saída
print('O salário com aumento de 25% é: ', salario_com_aumento)