def main():
    num = int(input('Digite um número de 2 dígitos: '))
    d, u = separar(num)
    dezena_unidade(d, u)


def separar(num):
    return num // 1 % 10, num // 10 % 10
    

def dezena_unidade(d, u):
    if d == u:
        print('O algarismo da dezena é igual ao algarismo da unidade.')
    else:
        print('O algarismo da dezena é diferente do algarismo da unidade.')


main()
