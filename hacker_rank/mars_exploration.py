def main():
    s = str(input())

    quant = marsExploration(s)
    print(quant)


def marsExploration(s):
    cont = 0
    tam_s = len(s)

    for c in range(tam_s):
        if c % 3 == 0 and s[c] != 'S':
            cont += 1
        if c % 3 == 1 and s[c] != 'O':
            cont += 1
        if c % 3 == 2 and s[c] != 'S':
            cont += 1

    return cont


main()