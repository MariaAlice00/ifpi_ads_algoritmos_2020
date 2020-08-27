def main():
    n = int(input('>>> '))

    x = 1
    s = 0

    while x <= n:
        y = 1 / x
        s = s + y
        x = x + 1
    
    print('S = {}'.format(s))

main()
