# Leia um número, calcule e escreva seu fatorial.

def main():
    num = int(input('>>> '))

    total = 1
    contador = 1
    
    while contador <= num:
        total = total * contador
        contador = contador + 1
        
    print(total)

main()
