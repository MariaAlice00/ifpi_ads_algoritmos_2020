'''Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.'''

def main():
    lim_inf = int(input('Primeiro número: '))
    lim_sup = int(input('Último número: '))

    print('Os números ímpares entre {} e {} são:'.format(lim_inf, lim_sup))

    x = lim_inf

    while x <= lim_sup:
        if x % 2 != 0:
            print(x)
        x += 1

main()
