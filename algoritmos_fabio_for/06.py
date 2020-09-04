'''Escreva a tabuada dos números de 1 a 10.'''

def main():
    num = int(input('Você quer saber a tabuada de que número? '))
    for c in range(1, 11):
        print('{} x {:2} = {:2}'.format(num, c, num*c))


main()
