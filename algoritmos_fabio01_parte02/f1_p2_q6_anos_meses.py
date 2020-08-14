# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

meses_inicial = int(input('Digite o valor em meses: '))

anos = meses_inicial // 12
meses_final = meses_inicial % 12

print('{} meses equivalem a {} ano(s) e {} meses'. format(meses_inicial, anos, meses_final))

