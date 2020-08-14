# Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo 
# para decidir o número de notas de cada valor que deve ser disponibilizado para o cliente 
# que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido 
# de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. 
# Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, 
# para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, 
# três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba 
# o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério 
# da distribuição ótima.

from time import sleep

valor = int(input('Digite o valor: R$ '))

cem = valor //100
resto = valor % 100
cinquenta = resto // 50
resto = resto % 50
vinte = resto // 20
resto = resto % 20
dez = resto // 10
resto = resto % 10
cinco = resto // 5
resto = resto % 5
dois = resto // 2

print('Processando...')
sleep(2)
print('******** VOCÊ IRÁ SACAR ********')
sleep(1)
print('>>> {} nota(s) de R$ 100'. format(cem))
sleep(1)
print('>>> {} nota(s) de R$ 50'. format(cinquenta))
sleep(1)
print('>>> {} nota(s) de R$ 20'. format(vinte))
sleep(1)
print('>>> {} nota(s) de R$ 10'. format(dez))
sleep(1)
print('>>> {} nota(s) de R$ 5'. format(cinco))
sleep(1)
print('>>> {} nota(s) de R$ 2'. format(dois))
sleep(1)
print('Obrigada por escolher nossos serviços!')
