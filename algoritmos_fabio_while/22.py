def main():
    n = int(input('Número de fichas: '))

    x = 1
    contador = 1
    num1 = 0
    num2 = 0
    maior = 0
    menor = 0
    c = 1

    while x <= n:
        print('-'*20)
        num = int(input('Número de identificação: '))
        nome = str(input('Nome: '))
        peso = float(input('Peso(kg): '))

        x += 1
        contador += 1
        if peso > maior:
            maior = peso
            num1 = num
        if peso < menor or c == 1:
            menor = peso
            num2 = num

        c += 1

    print('*'*8 + 'RESULTADO' + '*'*8)
    print('Boi mais gordo:')
    print('>>> Número de identificação: {}'.format(num1))
    print('>>> Peso: {} kg'.format(maior))
    print('Boi mais magro:')
    print('>>> Número de identificação: {}'.format(num2))
    print('>>> Peso: {} kg'.format(menor))

main()
