# não colocar símbolos e só minúsculas

string = str(input())
rotacao = int(input())

i = 0
while i < len(string):
    posicao = string[i]
    codigo = ord(posicao) + rotacao

    if codigo > 122:
        novo_codigo = codigo - 26
    elif codigo < 97:
        novo_codigo = codigo + 26
    else:
        novo_codigo = codigo

    nova_string = chr(novo_codigo)
    print(nova_string, end='') 

    i += 1