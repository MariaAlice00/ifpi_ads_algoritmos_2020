def main():
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))

    mmc = calcular_mmc(a, b)
    print('Achei: {}'.format())


def calcular_mmc(a, b):

    while True:
        if mmc % a == 0 and mmc % b == 0:
            print('Achei: {}'.format(mmc))
            break
        else:
            

main()