def main():
    N = int(input('>>> '))
    cont = 1
    valor = N
    s = 0

    while cont <= N:
        if cont % 2 == 0:
            s =  s - (valor/cont)
        else:
            s = s + (cont/valor)
        
        valor -= 1
        cont += 1

    print('S = {}'.format(s))

main()
