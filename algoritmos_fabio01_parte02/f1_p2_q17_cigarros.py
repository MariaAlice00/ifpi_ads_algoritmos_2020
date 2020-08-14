# Calcule a quantidade de dinheiro gasta por um fumante. 
# Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia 
# e o preço de uma carteira (1 carteira tem 20 cigarros).

anos = int(input('Há quantos anos você fuma?: '))
numero = int(input('Quantos cigarros você fuma por dia?: '))
carteira = float(input('Qual o preço de uma carteira de cigarro?: '))

x = (numero * carteira) / 20
y = 365 * anos
z = y * x

print('Você já gastou R$ {} em cigarros!'. format(z))


