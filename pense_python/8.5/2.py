# fazer a troca

string = str(input())
rotacao = int(input())

i = 0
while i < len(string):
    posicao = string[i]
    codigo = ord(posicao) + rotacao
    nova_string = chr(codigo)
    print(nova_string, end='')
    i += 1