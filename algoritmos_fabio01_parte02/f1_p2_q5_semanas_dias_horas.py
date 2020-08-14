# Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas 
# ele corresponde.

horas = int(input('Quantidade de horas: '))

semana = horas // 168
d_1 = horas % 168
d_2 = d_1 // 24
h = d_1 % 24


print('{} horas equivalem a {} semana(s) {} dia(s) e {} hora(s)'.format(horas, semana, d_2 , h))
