def main():
    n = int(input('Número de fichas: '))

    num1, num2, maior, menor = maior_menor(n)

    print('*'*8 + 'RESULTADO' + '*'*8)
    print('Boi mais gordo:')
    print('>>> Número de identificação: {}'.format(num1))
    print('>>> Peso: {} kg'.format(maior))
    print('Boi mais magro:')
    print('>>> Número de identificação: {}'.format(num2))
    print('>>> Peso: {} kg'.format(menor))


def maior_menor(n):
    contador = 1
    num1 = 0
    num2 = 0
    maior = 0
    menor = 0
    x = 1

    for c in range(1, n+1):
        print('-'*20)
        num = int(input('Número de identificação: '))
        nome = str(input('Nome: '))
        peso = float(input('Peso(kg): '))

        contador += 1
        if peso > maior:
            maior = peso
            num1 = num
        if peso < menor or x == 1:
            menor = peso
            num2 = num

        x += 1

    return num1, num2, maior, menor 


main()