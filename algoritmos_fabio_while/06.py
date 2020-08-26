# Escreva a tabuada dos números de 1 a 10.

def main():
    num = int(input('>>> '))

    print('-'*13)
    print('TABUADA DE {}'.format(num))
    print('-'*13)

    primeiro = 1
    ultimo = 10
    x = primeiro
    
    while x <= ultimo:
        print('{} x {:2} = {:2}'.format(num, x, x*num))
        x += 1

main()
