def main():
    print('DATA DO SEU NASCIMENTO')
    dia_nasc = int(input('Dia que você nasceu? '))
    mes_nasc = int(input('E o mês? '))
    ano_nasc = int(input('E o ano? '))

    print('DATA ATUAL')
    dia_atual = int(input('Que dia é hoje? '))
    mes_atual = int(input('E o mês? '))
    ano_atual = int(input('E o ano? '))

    print('Você tem {} anos, {} meses e {} dias'.format(ano(ano_atual, ano_nasc,mes_atual, mes_nasc), mes(mes_atual, mes_nasc), dia(dia_nasc, dia_atual, mes_nasc, mes_atual)))


def ano(ano_atual, ano_nasc,mes_atual, mes_nasc):
    if mes_atual >= mes_nasc:
        return ano_atual - ano_nasc
    else:
        return (ano_atual - ano_nasc) - 1


def mes(mes_atual, mes_nasc):
    if mes_atual < mes_nasc:
        return(mes_atual + 12) - mes_nasc
    else:
        return mes_atual - mes_nasc


def dia(dia_nasc, dia_atual, mes_nasc, mes_atual):
    return (30 - dia_nasc) + 30 * (mes(mes_atual, mes_nasc) - 1) + (30 - dia_atual)


main()