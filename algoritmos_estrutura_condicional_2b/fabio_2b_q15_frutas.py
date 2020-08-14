def main():
    morango = float(input('Quantidade de morangos, em kg: '))
    maça = float(input('Quantidade de maçãs, em kg: '))

    print('O valor a ser pago é: R$ {:.2f}'.format(valor_desconto(morango, maça)))


def valor_total_morango(morango):
    if morango <= 5:
        return 2.50 * morango
    else:
        return 2.20 * morango


def valor_total_maça(maça):
    if maça <= 5:
        return 1.80 * maça
    else: 
        return 1.50 * maça


def valor_total(morango, maça):
    return valor_total_morango(morango) + valor_total_maça(maça)


def valor_desconto(morango, maça):
    if morango + maça > 8 or valor_total(morango, maça) > 25:
        return valor_total(morango, maça) - 0.1 * valor_total(morango, maça)
    else:
        return valor_total(morango, maça)


main()