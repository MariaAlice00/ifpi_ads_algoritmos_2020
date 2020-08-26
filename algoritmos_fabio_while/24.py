def main():
    n = int(input('Número de habitantes: '))
    
    x = 1
    total_salario = 0
    total_filhos = 0
    soma_salario = 0
    soma_filhos = 0
    contagem_1000 = 0

    while x <= n:
        salario = float(input('Salário: R$ '))
        num_filhos = int(input('Números de filhos: '))
        print('*'*30)

        x += 1

        soma_salario += salario
        soma_filhos += num_filhos

        if salario <= 1000:
            contagem_1000 += 1

    print('Média de salário da população: {:.2f}'.format(soma_salario/n))
    print('Média de número de filhos: {:.1f}'.format(soma_filhos/n))
    print('{:.1f}% das pessoas tem salário de até R$ 1.000,00'.format((contagem_1000 * 100)/n))

main()
