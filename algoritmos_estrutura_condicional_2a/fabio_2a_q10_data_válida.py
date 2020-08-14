def main():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))

    data_valida(dia, mes, ano)


def data_valida(dia, mes, ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if mes == 4 or mes == 6 or mes == 9 or mes ==11 and dia <= 30:
            print('A data é válida')
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <= 31:
            print('A data é válida')
        elif mes == 2 and dia <=29:
            print('A data é válida')
        else:
            print('A data não é válida')
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia <= 30:
            print('A data é válida')
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <= 31:
            print('A data é válida')
        elif mes == 2 and dia <=28:
            print('A data é válida')
        else:
            print('A data não é válida')


main()