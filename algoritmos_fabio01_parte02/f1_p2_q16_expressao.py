# Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# d = (r + s) / 2, onde r = (a + b) ** 2 s = (b + c) ** 2

a = int(input('Digite um número positivo: '))
b = int(input('Digite um número positivo: '))
c = int(input('Digite um número positivo: '))

r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) / 2

print('O resultado da expressão é: ', d)
