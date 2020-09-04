# Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def main():
    primeiro = int(input('Primeiro: '))
    ultimo = int(input('Último: '))

    for c in range(primeiro,ultimo+1):
        for i in range(2, c):
            if (c % i == 0):
                break
        else:
            print(c, end=' ')


main()