# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...)

def main():
    n = int(input('>>> '))

    y = 1
    x = 2
    contador = 1
    p = 1
    
    print('{}'.format(1), end=' ')

    while True:
        y = y + x
        x = x + 1
        contador = contador + 1
        
        if contador > n:
            break
        
        print('-> {}'.format(y), end=' ')

main()
