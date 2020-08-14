def main():
    print('INÍCIO DO JOGO')
    hora_inicio = int(input('Digite a(s) hora(s), com dois digítos: '))
    minuto_inicio = int(input('Digite o(s) minuto(s), com dois digítos: '))
    print('FIM DO JOGO')
    hora_final = int(input('Digite a(s) hora(s), com dois digítos: '))
    minuto_final = int(input('Digite o(s) minuto(s), com dois digítos: '))

    print('DURAÇÃO DO JOGO: {}'.format(hora(hora_inicio, hora_final, minuto_inicio, minuto_final)))


def hora(hora_inicio, hora_final, minuto_inicio, minuto_final):
    if hora_final < hora_inicio:
        if minuto_final < minuto_inicio:
            h = (hora_final + 23) - hora_inicio
            m = (minuto_final + 60) - minuto_inicio
            return f'{h}h{m}min'
        else:
            h = (hora_final + 24) - hora_inicio
            m = minuto_final - minuto_inicio
            return f'{h}h{m}min'
    else:
        if minuto_final < minuto_inicio:
            h = (hora_final - 1) - hora_inicio
            m = (minuto_final + 60) - minuto_inicio
            return f'{h}h{m}min'
        else:
            h = hora_final - hora_inicio
            m = minuto_final - minuto_inicio
            return f'{h}h{m}min'


main()