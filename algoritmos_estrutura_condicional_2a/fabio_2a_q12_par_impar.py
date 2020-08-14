def main():
    num = int(input('Digite um número inteiro: '))
    par_impar(num)


def par_impar(num):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')


main()