# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos 
# segundos ele corresponde.

segundos = int(input('Quantidade de segundos: '))

h = segundos // 3600
m_1 = segundos % 3600
m_2 = m_1 // 60
s = m_1 % 60

print('{} segundos equivalem a {} hora(s) {} minuto(s) e {} segundo(s)'.format(segundos, h, m_2 , s))
