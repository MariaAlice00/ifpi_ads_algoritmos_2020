# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o maior quadrado menor que 38 é 36 (quadrado de 6).
n = int(input('>>> '))

x = 1
lista = []

while True:
    y = x * x
    x = x + 1
    if y > n:
        break
    
    lista.append(y)

print(max(lista))