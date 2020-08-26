def main():
    N = int(input('>>> '))

    d = 1
    calculo = 0
    contador = 0

    while d <= N:
        y = 1 / d
        contador = contador + 1 
        if contador % 2 != 0:
            calculo = calculo - y
        else:
            calculo = calculo + y

        d += 1

    print(calculo * -1)

main()
