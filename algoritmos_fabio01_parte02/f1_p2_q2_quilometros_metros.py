# Leia um valor inteiro de metros, calcule e escreva quantos quilômetros e quantos metros ele corresponde.

metro = int(input('Valor em metros: '))

km = metro // 1000
m = metro % 1000

print('{} metros correspondem a {} quilômetros e {} metros'.format(metro, km, m))
