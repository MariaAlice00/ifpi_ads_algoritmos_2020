def main():
    n = int(input('>>> '))

    x = 1
    soma = 0

    while x <= n:
        y = 1 / x
        soma = soma + y
        x = x + 1
    
    print(soma)

main()
