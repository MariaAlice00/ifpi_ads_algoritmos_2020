'''Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.'''
lim_sup = int(input('Limite superior: '))
lim_inf = int(input('Limite inferior: '))

x = lim_inf
while x <= lim_sup:
    if x % 2 != 0:
        print(x)
    x += 1