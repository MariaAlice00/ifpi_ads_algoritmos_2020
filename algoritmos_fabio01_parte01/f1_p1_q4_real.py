# Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$)

# Entrada
dolar_cotacao = float(input('Qual a cotação do dólar hoje? R$ '))
valor_dolar = float(input('Valor que você quer converter: US$ '))

# Processamento
valor_real = dolar_cotacao * valor_dolar 

# Saída
print('US$ {} equivalem a R$ {:.2f}'.format(valor_dolar, valor_real))