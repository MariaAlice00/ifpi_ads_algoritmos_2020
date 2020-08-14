def main():
    num_litros = int(input('Número de litros vendidos: '))
    tipo_combustivel = str(input('Tipo de combustível. Se for álcool, digite A, se for gasolina digite G: '))

    print('O valor a ser pago é: R$ {:.2f}'.format(abs(valor(num_litros, tipo_combustivel))))


def desconto_alcool(num_litros):
    if num_litros <= 20:
        return (3 * num_litros) / 100
    else:
        return (5 * num_litros) / 100


def desconto_gasolina(num_litros):
    if num_litros <= 20:
        return (4 * num_litros) / 100
    else:
        return (6 * num_litros) / 100


def valor(num_litros, tipo_combustivel):
    if tipo_combustivel == 'A':
        return (1.90 * num_litros) - (desconto_alcool(num_litros) * (1.90 * num_litros))
    else:
        return (2.50 * num_litros) - (desconto_gasolina(num_litros) * (2.50 * num_litros))
    

main()