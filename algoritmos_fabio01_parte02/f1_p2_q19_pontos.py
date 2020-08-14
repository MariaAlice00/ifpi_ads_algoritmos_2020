# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, 
# ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme a fórmula.

x_1 = int(input('Digite a abscissa do ponto 1: '))
y_1 = int(input('Digite a ordenada do ponto 1: '))
x_2 = int(input('Digite a abscissa do ponto 2: '))
y_2 = int(input('Digite a ordenada do ponto 2: '))

d1 = (x_2 - x_1) ** 2 
d2 = (y_2 - y_1) ** 2
d = d1 + d2
D = d ** (1/2)

print('A distância entre os pontos é igual a {:.2f}'.format(D))

