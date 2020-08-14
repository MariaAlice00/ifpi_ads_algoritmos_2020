from time import sleep

def main():
    valor_hora = float(input('Valor da hora: '))
    quant_horas = int(input('Quantidade de horas trabalhadas por mês: '))

    print('PROCESSANDO...')
    sleep(2)
    print('SALÁRIO BRUTO (R$ {:.2f} * {}) >>> R$ {}'.format(valor_hora, quant_horas, salario_bruto(valor_hora, quant_horas)))
    sleep(1)
    print('(-)IMPOSTO DE RENDA ({}) >>> R$ {:.2f}'.format(imposto_renda_valor(salario_bruto, valor_hora, quant_horas),imposto_renda_calculo(salario_bruto, valor_hora, quant_horas)))
    sleep(1)
    print('(-)SINDICATO (3%) >>> R$ {:.2f}'.format(sindicato(salario_bruto,valor_hora, quant_horas)))
    sleep(1)
    print('FGTS >>> R$ {:.2f}'.format(fgts(salario_bruto, valor_hora, quant_horas)))
    sleep(1)
    print('TOTAL DE DESCONTOS >>> R$ {:.2f}'.format(descontos(salario_bruto, valor_hora, quant_horas)))
    sleep(1)
    print('SALÁRIO LÍQUIDO >>> R$ {:.2f}'.format(salario_liquido(valor_hora, quant_horas)))


def salario_bruto(valor_hora, quant_horas):
    return valor_hora * quant_horas


def sindicato(salario_bruto, valor_hora, quant_horas):
    return 0.03 * salario_bruto(valor_hora, quant_horas)


def fgts(salario_bruto, valor_hora, quant_horas):
    return 0.11 * salario_bruto(valor_hora, quant_horas)


def descontos(salario_bruto, valor_hora, quant_horas):
    return imposto_renda_calculo(salario_bruto, valor_hora, quant_horas) + sindicato(salario_bruto, valor_hora, quant_horas)


def salario_liquido(valor_hora, quant_horas):
    return salario_bruto(valor_hora, quant_horas) - descontos(salario_bruto, valor_hora, quant_horas)


def imposto_renda_valor(salario_bruto, valor_hora, quant_horas):
    if salario_bruto(valor_hora, quant_horas) <= 900:
        return '0%'
    elif salario_bruto(valor_hora, quant_horas) > 900 and salario_bruto(valor_hora, quant_horas) <= 1500:
        return '5%'
    elif salario_bruto(valor_hora, quant_horas) > 1500 and salario_bruto(valor_hora, quant_horas) <= 2500:
        return '10%'
    else:
        return '20%'

def imposto_renda_calculo(salario_bruto, valor_hora, quant_horas):
    if salario_bruto(valor_hora, quant_horas) <= 900:
        return salario_bruto(valor_hora, quant_horas) * 0
    elif salario_bruto(valor_hora, quant_horas) > 900 and salario_bruto(valor_hora, quant_horas) <= 1500:
        return salario_bruto(valor_hora, quant_horas) * 0.05
    elif salario_bruto(valor_hora, quant_horas) > 1500 and salario_bruto(valor_hora, quant_horas) <= 2500:
        return salario_bruto(valor_hora, quant_horas) * 0.1
    else:
        return salario_bruto(valor_hora, quant_horas) * 0.2


main()