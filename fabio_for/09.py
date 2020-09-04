'''Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.'''

def main():
    lim_inf = int(input('Primeiro: '))
    lim_sup = int(input('Último: '))

    for c in range(lim_inf, lim_sup+1):
        if c % 2 == 0:
            print(c)

main()