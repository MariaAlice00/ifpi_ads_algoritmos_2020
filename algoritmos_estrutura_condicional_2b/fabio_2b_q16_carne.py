import time

def main():
    tipo = str(input('Tipo de carne: filé, alcatra ou picanha? '))
    quant = float(input('Quantos kg? '))
    cartao_dinheiro = str(input('Vai pagar com cartão ou dinheiro? '))

    print('AGUARDE...')
    time.sleep(2)
    print('TIPO: {}'.format(tipo))
    time.sleep(1)
    print('QUANTIDADE: {} kg'.format(quant))
    time.sleep(1)
    print('PREÇO TOTAL: R$ {:.2f}'.format(valor_carne(tipo, quant)))
    time.sleep(1)
    print('TIPO DE PAGAMENTO: {}'.format(cartao_dinheiro))
    time.sleep(1)
    print('VALOR DO DESCONTO: R$ {:.2f}'.format(valor_do_desconto(cartao_dinheiro, tipo, quant)))
    time.sleep(1)
    print('VALOR A PAGAR: R$ {:.2f}'.format(valor_com_desconto(cartao_dinheiro, tipo, quant)))


def valor_carne(tipo, quant):
    if tipo == 'filé':
        if quant <= 5:
            return 4.90 * quant
        else:
            return 5.80 * quant
    elif tipo == 'alcatra':
        if quant <= 5:
            return 5.90 * quant
        else:
            return 6.80 * quant
    else:
        if quant <= 5:
            return 6.90 * quant
        else:
            return 7.80 * quant


def valor_do_desconto(cartao_dinheiro, tipo, quant):
    if cartao_dinheiro == 'cartão':
        return 0.05 * valor_carne(tipo, quant)
    else:
        return 0


def valor_com_desconto(cartao_dinheiro, tipo, quant):
    if cartao_dinheiro == 'cartão':
        return valor_carne(tipo, quant) - (0.05 * valor_carne(tipo, quant))
    else:
        return valor_carne(tipo, quant)


main()