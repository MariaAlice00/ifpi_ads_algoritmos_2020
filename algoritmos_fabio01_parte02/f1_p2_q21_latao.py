# Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo 
# que calcule a quantidade de cada um desses componentes para se obter certa quantidade 
# de latão (em kg), informada pelo usuário.

latao = float(input('Qual a quantidade desejada de latão, em kg: '))

cobre = 0.7 * latao
zinco = 0.3 * latao

print('Você terá {} kg de cobre e {} kg de zinco'.format(cobre, zinco))
