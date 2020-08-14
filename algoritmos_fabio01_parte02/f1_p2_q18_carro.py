# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem 
# do distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, 
# escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input('Digite o custo de fábrica: '))

distribuidor = 0.28 * custo_fabrica
imposto = 0.45 * custo_fabrica
custo_consumidor = custo_fabrica + distribuidor + imposto

print('O custo do carro novo é de R$: {:.2f}'.format(custo_consumidor))
