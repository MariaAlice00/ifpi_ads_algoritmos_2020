'''Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lido'''

def main():
    n = int(input('>>> '))
    lim_inf = int(input('Primeiro termo: '))
    lim_sup = int(input('Último termo: '))

    print('Os múltiplos de {} entre {} e {} são:'.format(n, lim_inf, lim_sup))

    x = lim_inf

    while x <= lim_sup:
        if x % n == 0:
            print(x)
        x = x + 1

main()
