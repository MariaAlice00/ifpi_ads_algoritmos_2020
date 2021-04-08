def main():
    # ponto de partida; contador, somatorio, qtd_num
    contador = 0
    somatorio = 0
    qtd_num = 0   
    num = int(input('Número: ')) # estado anterior

    while num >= 0:
        somatorio = somatorio + num
        qtd_num = qtd_num + 1
        num = int(input('Número: '))

    # mostrar a média
    if qtd_num > 1:
        media = somatorio / qtd_num
        print('Média: {}'.format(media))

main()