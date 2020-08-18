'''Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lido'''

n = int(input('N: '))
lim_inf = int(input('Limite inferior: '))
lim_sup = int(input('Limite superior: '))

x = lim_inf
while x <= lim_sup:
    if x % n == 0:
        print(x)
    x = x + 1
