def numeros_iguais(a, b, c):
    if a == b == c:
        print('Todos os números são iguais.')
    elif a == b != c or a == c != b or b == c != a:
        print('2 números são iguais.')
    else:
        print('Todos os números são diferentes.')
    
def main():
    a = int(input('Digite 1º número inteiro: '))
    b = int(input('Digite 2º número inteiro: '))
    c = int(input('Digite 3º número inteiro: '))

    numeros_iguais(a, b, c)

main()
