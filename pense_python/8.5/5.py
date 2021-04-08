# Com funções

def rotate_world(string, rotacao):
    i = 0
    while i < len(string):
        posicao = string[i]
        codigo = ord(posicao) + rotacao

        if posicao.islower() == True:
            if codigo > 122:
                novo_codigo = codigo - 26
            elif codigo < 97:
                novo_codigo = codigo + 26
            else:
                novo_codigo = codigo

        elif posicao.isupper() == True:
            if codigo > 90:
                novo_codigo = codigo - 26
            elif codigo < 65:
                novo_codigo = codigo + 26
            else:
                novo_codigo = codigo

        nova_string = chr(novo_codigo)
        print(nova_string, end='')
        
        i += 1

def main():
    print('>>> Que palavra você quer rotacionar?')
    string = str(input())
    print('>>> Qual valor?')
    rotacao = int(input())

    print('*'*20)
    print('Processando...')
    from time import sleep
    sleep(2)
    print('A nova palavra é:')
    rotate_world(string, rotacao)


main()