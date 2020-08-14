# Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior 
# ou igual a cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. 
# Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais 
# a R$ 90,00; se o valor da mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações 
# são iguais a R$ 100,00. Escreva um algoritmo que receba o valor da mercadoria e forneça o valor 
# da entrada e das duas prestações, de acordo com as regras acima.

from time import sleep

valor = float(input('Digite o valor: R$ '))

entrada1 = valor // 3
entrada2 = valor % 3
entrada = entrada1 + entrada2
prestacao = (valor - entrada) / 2

print('='*10 + ' NOTA DA COMPRA ' + '='*10)
print('AGUARDE...')
sleep(2)
print('TOTAL DA COMPRA: R$ {:.2f}'.format(valor))
sleep(1)
print('ENTRADA: R$ {:.2f}'.format(entrada))
sleep(1)
print('PRESTAÇÕES: 2x de R$ {:.2f}.'.format(prestacao))
sleep(1)
print('='*5 + ' OBRIGADA PELA PREFERÊNCIA ' + '='*5)
