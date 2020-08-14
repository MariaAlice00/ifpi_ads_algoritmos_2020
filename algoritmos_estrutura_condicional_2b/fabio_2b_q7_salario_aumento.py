from time import sleep

def main():
    salario = float(input('Digite seu salário: R$ '))

    print('PROCESSANDO...')
    sleep(2)
    print('>>> SALÁRIO ANTES DO REAJUSTE: R$ {:.2f}'.format(salario))
    sleep(1)
    print('>>> PERCENTUAL DE AUMENTO APLICADO: {}'.format(percentual(salario)))
    sleep(1)
    print('>>> VALOR DO AUMENTO: R$ {:.2f}'.format(aumento(salario)))
    sleep(1)
    print('>>> NOVO SALÁRIO, APÓS AUMENTO: R$ {:.2f}'.format(novo_salario(salario)))
   

def percentual(salario):
    if salario <= 280:
        return '20%'
    elif salario > 280 and salario <= 700:
        return '15%'
    elif salario > 700 and salario < 1500:
        return '10%'
    else:
        return '5%'


def aumento(salario):
    if salario <= 280:
        return salario * 0.2
    elif salario > 280 and salario <= 700:
        return salario * 0.15
    elif salario > 700 and salario < 1500:
        return salario * 0.1
    else:
        return salario * 0.05


def novo_salario(salario):
    if salario <= 280:
        return salario + (salario * 0.2)
    elif salario > 280 and salario <= 700:
        return salario + (salario * 0.15)
    elif salario > 700 and salario < 1500:
        return salario + (salario * 0.1)
    else:
        return salario + (salario * 0.05)


main()