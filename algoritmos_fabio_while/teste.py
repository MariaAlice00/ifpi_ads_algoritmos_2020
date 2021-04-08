# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o maior quadrado menor que 38 é 36 (quadrado de 6).

def main():
    n = int(input('>>> '))

    x = 1
    lista = []

    for c in range(0, n+1):
        y = c * c
        
        lista.append(c)

    print(max(lista))

main()