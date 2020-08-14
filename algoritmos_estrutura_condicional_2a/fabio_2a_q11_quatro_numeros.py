def main():
    opção = int(input('Digite um número que seja 1, 2 ou 3: '))
    num1 = int(input('Digite outro número: '))
    num2 = int(input('Digite outro número: '))
    num3 = int(input('Digite outro número: '))
    
    valores(opção, num1, num2, num3)


def valores(opção, num1, num2, num3):
    if opção == 1:
        print(num1)
    elif opção == 2:
        print(num2)
    else:
        print(num3)


main()