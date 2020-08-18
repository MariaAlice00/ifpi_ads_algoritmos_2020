# Escreva a tabuada dos números de 1 a 10.

num = int(input('>>> '))
primeiro = 1
ultimo = 10
x = primeiro

while x <= ultimo:
    print('{} x {:2} = {:2}'.format(num, x, x*num))
    x += 1
