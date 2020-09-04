'''Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.'''

def main():
    n = int(input('>>> '))
    soma = 0
    for c in range(1, n+1):
        soma = soma + c
    print(soma)

main()