def calculo(num_horas, num_dependentes):
    salario_bruto = (num_horas * 12) + (num_dependentes * 40)
    inss = salario_bruto * 0.085
    ir = salario_bruto * 0.05
    salario_liquido = salario_bruto - inss - ir
    
    return inss, ir, salario_liquido

def main():
    n = int(input('Número de funcionários: '))
    x = 1

    while x <= n:
        print('-'*20)
        codigo = int(input('Código: '))
        num_horas = int(input('Número de horas trabalhadas: '))
        num_dependentes = int(input('Número de dependentes: '))
        print('-'*20)

        x += 1

        inss, ir, salario_liquido = calculo(num_horas, num_dependentes)

        print('INSS: R$ {:.2f}'.format(inss))
        print('IR: R$ {:.2f}'.format(ir))
        print('Salário líquido: R$ {:.2f}'.format(salario_liquido))

    print('FIM')

main()
