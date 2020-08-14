# Leia um valor em real (R$), calcule e escreva 70% deste valor.

# Entrada
valor = float(input('Digite o valor: R$ '))

# Processamento
valor_70 = 0.7 * valor

# Saída
print('70% de R$ {:.2f} equivalem a R$ {:.2f}'.format(valor, valor_70))