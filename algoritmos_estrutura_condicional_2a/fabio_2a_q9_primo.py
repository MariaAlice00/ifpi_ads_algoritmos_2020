def main():
    num = int(input('Digite um número entre 0 e 100: '))
    num_primos(num)


def num_primos(num):
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
        print('É PRIMO')
    elif num % 2 == 0:
        print('NÃO É PRIMO')
    elif num % 3 == 0:
        print('NÃO É PRIMO')
    elif num % 5 == 0:
        print('NÃO É PRIMO')
    elif num % 7 == 0:
        print('NÃO É PRIMO')
    elif num % 11 == 0:
        print('NÃO É PRIMO')
    else:
        print('É PRIMO')


main()