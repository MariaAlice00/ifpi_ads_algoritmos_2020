# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.

def main():
    a0 = int(input('Primeiro termo: '))
    limite = int(input('Limite: '))
    razao = int(input('Razão: '))

    while a0 < limite:
        a0 = a0 * razao
        if a0 >= limite:
            break
        print(a0)

main()
