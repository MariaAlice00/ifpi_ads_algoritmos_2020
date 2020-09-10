def main():
    print('>>> Que palavra você quer rotacionar?')
    string = input()
    print('>>> Qual valor?')
    rotacao = int(input())

    print('*'*20)
    print('Processando...')
    from time import sleep
    sleep(2)
    print('A nova palavra é:')
    print(rotate_world(string, rotacao))


def rotate_world(string, rotacao):
    i = 0
    texto = ''

    while i < len(string):
        posicao = string[i]
        codigo = ord(posicao) + rotacao

        if letra(posicao):
            if minuscula(posicao):
                if codigo > 122:
                    novo_codigo = codigo - 26
                elif codigo < 97:
                    novo_codigo = codigo + 26
                else:
                    novo_codigo = codigo
            elif maiuscula(posicao):
                if codigo > 90:
                    novo_codigo = codigo - 26
                elif codigo < 65:
                    novo_codigo = codigo + 26
                else:
                    novo_codigo = codigo

            nova_string = chr(novo_codigo)
        else:
            nova_string = posicao
        
        texto += nova_string    

        i += 1
    
    return texto


def letra(posicao):
    return minuscula(posicao) or maiuscula(posicao)


def minuscula(posicao):
    return ord(posicao) >= 97 and ord(posicao) <= 122


def maiuscula(posicao):
    return ord(posicao) >= 65 and ord(posicao) <= 90


main()
