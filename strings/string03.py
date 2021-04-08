def main():
    frase = input('Frase: ')
    palavra = input('Palavra: ')

    if contem(frase, palavra): # se a frase contém a palavra
        print('Sim. Palavra encontrada na frase')
    else:
        print('Não. A frase não contém a palavra')


def contem(frase, palavra):
    tam_frase = len(frase)
    tam_palavra = len(palavra)

    for pos in range((tam_frase-tam_palavra)+1):
        if frase[pos] == palavra:
            fatia = substring(frase, pos, tam_palavra) # retornar um pedaço de um texto
            if fatia == palavra:    
                return True
    return False


def substring(frase, pos, tam_palavra):


main()