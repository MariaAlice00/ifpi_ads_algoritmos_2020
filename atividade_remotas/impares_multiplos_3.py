def main():
    qtd_multiplos = 0
    #inicialização/estado inicial
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = inicio

    while atual <= fim: #condi. de continuidade
        #trabalho
        if atual % 3 == 0 and atual % 2 != 0:
            qtd_multiplos += 1
            print('>>> {}'.format(atual))

        # convergência do estado
        atual += 1

    print('Foram encontrados {} números múltiplos de 3 ímpares'.format(qtd_multiplos))

main()