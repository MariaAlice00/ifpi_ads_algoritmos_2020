'''Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.'''

def main():
    n = int(input('N: '))
    lim_inf = int(input('Primeiro: '))
    lim_sup = int(input('Último: '))

    for c in range(lim_inf, lim_sup+1):
        if c % n == 0:
            print(c)

main()