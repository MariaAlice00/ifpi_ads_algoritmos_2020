# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

print('-'*10 + 'SEQUÊNCIA DE FIBONACCI' + '-'*10)
num = int(input('>>> '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')

'''contador = 3, porque ja colocamos 2 termos'''
contador = 3

while contador <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' -> {}'.format(t3), end='')
    contador = contador + 1
