def main():
    frase = input('Frase: ')
    palavra = input('Palavra: ')

    if contem(frase, palavra): # se a frase contém a palavra
        print('Sim. Palavra encontrada na frase')
    else:
        print('Não. A frase não contém a palavra')


def contem(frase, palavra):
    if palavra in frase:
        return True
    else:
        return False
    
    '''return palavra in frase'''


main()