# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.

def main():
    A0 = int(input('Primeiro termo: '))
    limite = int(input('Último número: '))
    r = int(input('Razão: '))

    print(A0)
    y = A0

    for c in range(A0, limite):
        y = y * r

        if y < limite:
            print(y)


main()