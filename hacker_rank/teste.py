def main():
    q = int(input())

    for c in range(q):
        s = str(input())

        resposta = funny_string(s)
        print(funny_string(s))


def funny_string(s):
    p = ord(s[0])
    s = ord(s[1])
    ultimo = len(s) - 1
    while s <= ultimo:
        dif = p - s
        p += 1
        s += 1   
        print(dif)     



def inverso(s):
    inv = ''

    for c in range(len(s)-1, -1, -1):
        inv += s[c]

    return inv




main()