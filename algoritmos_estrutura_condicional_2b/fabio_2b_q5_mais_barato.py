def main():
    produto1 = float(input('Preço do primeiro produto: '))
    produto2 = float(input('Preço do segundo produto: '))
    produto3 = float(input('Preço do terceiro produto: '))

    mais_barato(produto1, produto2, produto3)


def mais_barato(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        print('Você deve comprar o primeiro produto.')
    elif produto2 < produto1 and produto2 < produto3:
        print('Você deve comprar o segundo produto.')
    else:
        print('Você deve comprar o terceiro produto.')
    

main()