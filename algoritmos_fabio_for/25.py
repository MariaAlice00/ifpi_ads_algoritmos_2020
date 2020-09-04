def main():
    n = int(input('Número de eleitores: '))

    print('******** VOTAÇÃO ********')
    print('Digite:')
    print('1 - para o candidato A')
    print('2 - para o candidato B')
    print('3 - para o candidato C')
    print('9 - nulo')
    print('0 - em branco')

    total_a, total_b, total_c, total_nulos, total_branco = voto(n)

    print('******** RESULTADO ********')
    print('Candidato A: {}'.format(total_a))
    print('Candidato B: {}'.format(total_b))
    print('Candidato C: {}'.format(total_c))
    print('Nulos: {}'.format(total_nulos))
    print('Em branco: {}'.format(total_branco))
    print('*'*20)    
    print('O candidato eleito é...')

    print(maior(total_a, total_b, total_c, total_branco, total_nulos))
    
    print('Obrigada por votar!!!')


def voto(n):
    total_a = 0
    total_b = 0
    total_c = 0
    total_nulos = 0
    total_branco = 0

    for c in range(1, n+1):
        voto = int(input('>>> '))
        
        if voto == 1:
            total_a += 1
        elif voto == 2:
            total_b += 1
        elif voto == 3:
            total_c += 1
        elif voto == 9:
            total_nulos += 1
        elif voto == 0:
            total_branco += 1

    return total_a, total_b, total_c, total_nulos, total_branco


def maior(total_a, total_b, total_c, total_branco, total_nulos):
    maior = total_a

    if total_b > total_a:
        maior = total_b
        return 'Candidato B'
    elif total_c > total_a:
        maior = total_c
        return 'Candidato C'
    else:
        return 'Candidato A'


main()
