# Um sistema de equações lineares do tipo ax + by = c e dx + ey = f, 
# pode ser resolvido segundo mostrado abaixo:
# x = ce - bf / ae -  bd 
# y = af - cd / ae - bd
# Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, 
# calcule e escreva os valores de x e y.

a = int(input('Valor a: '))
b = int(input('Valor b: '))
c = int(input('Valor c: '))
d = int(input('Valor d: '))
e = int(input('Valor e: '))
f = int(input('Valor f: '))

x_1 = (c * e) - (b * f) 
x_2 = (a * e) - (b * d)
x = x_1 / x_2
y_1 = (a * f) - (c * d) 
y_2 = (a * e) - (b * d)
y = y_1 / y_2

print('O valor de x é {} e de y é {}'.format(x, y))
