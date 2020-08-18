# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.
a0 = int(input('Primeiro termo: '))
limite = int(input('Limite: '))
razao = int(input('Razão: '))

pg = a0 * razao
print(pg, end=' ')

while pg < limite:
    pg = pg * razao

    print(pg, end=' ')

while True:
    pg = pg * razao

    print(pg, end=' ')

    if pg >= limite:
        break
