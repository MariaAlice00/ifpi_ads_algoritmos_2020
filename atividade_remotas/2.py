num_secreto = 12
tentativas = 3

while tentativas > 0: # quando chegar a 0 para.
    chute = int(input('Digite um número entre 0 e 20: '))

    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto

    if acertou:
        print('Você acertou!!!')
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto')

    tentativas = tentativas - 1 # atualização, para o loop não ser infinito