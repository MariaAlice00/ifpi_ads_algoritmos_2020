# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

dias = int(input('Quantidade de dias: '))

s = dias // 7
d = dias % 7

print('{} dias correspondem a {} semana(s) {} dias(s)'. format(dias, s, d))
