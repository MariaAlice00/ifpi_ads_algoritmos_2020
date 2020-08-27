def main():
    N = int(input('>>> '))

    d = 1
    s = 0
    contador = 0

    while d <= N:
        y = 1 / d
        contador = contador + 1 
        
        if contador % 2 != 0:
            s = s - y
        else:
            s = s + y

        d += 1

    print('S = {}'.format(s * -1))

main()
