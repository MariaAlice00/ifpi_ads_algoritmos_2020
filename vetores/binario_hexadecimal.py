'''Leia um número (vetor com 8 elementos) na base binária, calcule e escreva este número na base hexadecimal e na base decimal.'''

def main():
    binario = int(input('Número binário: '))

    decimal = transformar_decimal(binario)
    print('Base decimal: {}'.format(decimal))

    hexadecimal = transformar_hexadecimal(binario)
    print('Base hexadecimal: ',end='')
    for h in hexadecimal:
        print(h, end='')


def transformar_em_vetor(binario):
    binario = str(binario)
    num_str = []
    for c in range(len(binario)):
        num_str.append(binario[c])

    return num_str


def transformar_decimal(binario):
    num_str = transformar_em_vetor(binario)

    c = len(num_str) - 1
    decimal = 0
    
    for num in num_str:
        num = int(num)
        num = num * (2 ** c)
        decimal += num
        
        c -= 1

    return decimal


def transformar_hexadecimal(binario):
    decimal = transformar_decimal(binario)
    num = decimal
    p = num % 16
    resto = [p]

    while True:
        if num < 16:
            break

        num = num // 16
        r = num % 16
        resto.append(r)

    h = []
    for n in resto:
        n = int(n)
        n = hexadecimal(n)
        h.append(n)

    h = h[::-1]
    return h



def hexadecimal(n):
    if n >= 0 and n <= 9:
        n = n
    else:
        if n == 10:
            n = 'A'
        if n == 11:
            n = 'B'
        if n == 12:
            n = 'C'
        if n == 13:
            n = 'D'
        if n == 14:
            n = 'E'
        if n == 15:
            n = 'F'

    return n


if __name__ == "__main__":
    main()