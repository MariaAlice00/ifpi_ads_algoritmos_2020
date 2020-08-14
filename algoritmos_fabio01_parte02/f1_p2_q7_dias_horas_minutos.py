# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

minuto = int(input('Digite o número em minutos: '))

dias = minuto // 1440
horas = minuto % 1440 // 60
minutos = horas % 60

print(f'{minuto} minutos equivalem a {dias} dia(s) {horas} horas(s) e {minutos} minuto(s)')