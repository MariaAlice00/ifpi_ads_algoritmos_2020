'''Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A0 e razão R.'''

def main():
    a0 = int(input('Primeiro termo: '))
    limite = int(input('Último termo: '))
    r = int(input('Razão: '))

    for c in range(a0, limite, r):
        print(c)

main()