def main():
    n = int(input('Número de habitantes: '))
    
    soma_salario, soma_filhos, contagem_1000 = conta(n)

    print('Média de salário da população: {:.2f}'.format(media_salario(soma_salario, n)))
    print('Média de número de filhos: {}'.format(media_filhos(soma_filhos, n)))
    print('{:.1f} % das pessoas tem salário de até R$ 1.000,00'.format(salario_ate_1000(contagem_1000, n)))


def conta(n):
    total_salario = 0
    total_filhos = 0
    soma_salario = 0
    soma_filhos = 0
    contagem_1000 = 0

    for c in range(1, n+1):
        salario = float(input('Salário: R$ '))
        num_filhos = int(input('Números de filhos: '))
        print('*'*30)

        soma_salario += salario
        soma_filhos += num_filhos

        if salario <= 1000:
            contagem_1000 += 1

    return soma_salario, soma_filhos, contagem_1000


def media_salario(soma_salario, n):
    return soma_salario/n

def media_filhos(soma_filhos, n):
    return soma_filhos/n

def salario_ate_1000(contagem_1000, n):
    return (contagem_1000 * 100)/n


main()