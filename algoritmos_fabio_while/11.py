primeiro = int(input('Primeiro: '))
ultimo = int(input('Último: '))

contador = 1
x = 0
while primeiro < ultimo:
    y = primeiro - 1
    while y > 1:
        if primeiro % y == 0:
            break
        y = y - 1
        contador = contador + 1
    else:
        print(primeiro, end=' ')
        x = x + 1
    primeiro = primeiro + 1

