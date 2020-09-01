# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A0 e razão R.

def main():
    A0 = int(input('Primeiro termo: '))
    limite = int(input('Último número: '))
    r = int(input('Razão: '))

    p = A0
    while p < limite:
        print(p)
        p += r

main()
