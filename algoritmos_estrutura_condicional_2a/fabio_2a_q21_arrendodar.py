def main():
    num = float(input('Digite um número decimal: '))
    
    print(arrendondar(num))


def inteiro(num):
    return int(num)


def arrendondar(num):
    if (num - inteiro(num)) >= 0.5:
        return inteiro(num) + 1
    else:
        return inteiro(num) - 1


main()