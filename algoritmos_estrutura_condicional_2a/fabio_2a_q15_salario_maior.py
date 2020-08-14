def main():
    hora_prof_1 = int(input('Quantas horas aula o primeiro professor ministra?  '))    
    hora_prof_2 = int(input('Quantas horas aula o segundo professor ministra?  ')) 
    valor_prof_1 = float(input('Valor hora recebido pelo primeiro professor: R$ '))
    valor_prof_2 = float(input('Valor hora recebido pelo segundo professor: R$ '))

    salario(hora_prof_1, hora_prof_2, valor_prof_1, valor_prof_2)


def salario(hora_prof_1, hora_prof_2, valor_prof_1, valor_prof_2):
    salario_prof_1 = hora_prof_1 * valor_prof_1 * 20
    salario_prof_2 = hora_prof_2 * valor_prof_2 * 20
    if salario_prof_1 > salario_prof_2:
        print('O primeiro professor tem o salário maior, com R$ {:.2f}!!!'.format(salario_prof_1))
    elif salario_prof_2 > salario_prof_1:
        print('O segundo professor tem o salário maior, com R$ {:.2f}!!!'.format(salario_prof_2))
    else:
        print('Os dois professores tem o salário igual, com R$ {:.2f}!!!'.format(salario_prof_1))


main()
