nome = 'Maria Alice'
# inicialização/estado anterior
contador = 0
alvo = 10

print('Início...')

while contador < alvo: # condição de continuidade
    # trabalho
    print('Olá {} tudo bem?'.format(nome))

    # convergência do estado / atualização
    contador = contador + 1

print('Fim...')