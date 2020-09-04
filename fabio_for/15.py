# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...)

def main():
    n = int(input('>>> '))

    y = 1
    
    print('{}'.format(1), end=' ')

    for c in range(2, n+1):
        y = y + c
        
        print('-> {}'.format(y), end=' ')

main()