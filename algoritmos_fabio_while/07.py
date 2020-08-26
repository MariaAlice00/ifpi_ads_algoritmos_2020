'''Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.'''

def main():
    n = int(input('>>> '))

    total = 0
    contador = 1
    
    while contador <= n:
        total = total + contador
        contador = contador + 1
    
    print(total)

main()
