'''Leia um número, calcule e escreva seu fatorial.'''

def main():
    num = int(input('>>> '))
    x = 1

    for c in range(1, num+1):
        x = x * c

    print(x)

main()