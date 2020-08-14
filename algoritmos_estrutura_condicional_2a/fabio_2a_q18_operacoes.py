def main():
    num1 = float(input('Primeiro valor: '))
    num2 = float(input('Segundo valor: '))
    op = int(input('Digite 1, 2, 3 ou 4: '))
    
    operacao(num1, num2, op)


def operacao(num1, num2, op):
    if op == 1:
        print(num1 + num2)
    elif op == 2:
        print(num1 - num2)
    elif op == 3:
        print(num1 * num2)
    else:
        print(num1 / num2)

    
main()