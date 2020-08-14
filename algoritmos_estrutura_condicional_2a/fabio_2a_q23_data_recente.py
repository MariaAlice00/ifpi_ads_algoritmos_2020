def main():
    print('DATA 1')
    dia1 = int(input('Dia: '))
    mes1 = int(input('Mês: '))
    ano1 = int(input('Ano: '))
    print('DATA 2')
    dia2 = int(input('Dia: '))
    mes2 = int(input('Mês: '))
    ano2 = int(input('Ano: '))

    print('DATA MAIS RECENTE: {}'.format(data_recente(dia1, mes1, ano1, dia2, mes2, ano2)))


def data_recente(dia1, mes1, ano1, dia2, mes2, ano2):
    if dia1 == dia2 and mes1 > mes2 and ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia1 > dia2 and mes1 == mes2 and ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia1 > dia2 and mes1 > mes2 and ano1 == ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia1 == dia2 and mes1 == mes2 and ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia1 > dia2 and mes1 == mes2 and ano1 == ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia1 == dia2 and mes1 > mes2 and ano1 == ano2:
        return f'{dia1}/{mes1}/{ano1}'
    else:
        return f'{dia2}/{mes2}/{ano2}'


main()