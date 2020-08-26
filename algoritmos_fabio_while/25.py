def main():
    n = int(input('Número de eleitores: '))

    print('******** VOTAÇÃO ********')
    print('Digite:')
    print('1 - para o candidato A')
    print('2 - para o candidato B')
    print('3 - para o candidato C')
    print('9 - nulo')
    print('0 - em branco')

    x = 1
    total_a = 0
    total_b = 0
    total_c = 0
    total_nulos = 0
    total_branco = 0

    while x <= n:
        voto = int(input('>>> '))
        x += 1
        
        if voto == 1:
            total_a += 1
        elif voto == 2:
            total_b += 1
        if voto == 3:
            total_c += 1
        if voto == 9:
            total_nulos += 1
        if voto == 0:
            total_branco += 1

    print('******** RESULTADO ********')
    print('Candidato A: {}'.format(total_a))
    print('Candidato B: {}'.format(total_b))
    print('Candidato C: {}'.format(total_c))
    print('Nulos: {}'.format(total_nulos))
    print('Em branco: {}'.format(total_branco))
    print('O candidato eleito é...')

    maior = max(total_a, total_b, total_c)
    if maior == total_a:
        print('Candidato A')
    elif maior == total_b:
        print('Candidato B')
    elif maior == total_c:
        print('Candidato C')

main()
