def main():
    q = int(input())
    
    for c in range(q):  
        s = input()

        resposta = funny_string(s)
        print(resposta)


def funny_string(s):
    tam_s = len(s)
    inv_s = inverso(s)

    for d in range(0, tam_s):
        dif = ord(s[d]) - ord(s[d-1])
        if dif < 0:
            dif = dif * -1
        
        dif_inv = ord(inv_s[d]) - ord(inv_s[d-1])
        if dif_inv < 0:
            dif_inv = dif_inv * -1

        if dif != dif_inv:
            return 'Not Funny'

    else:
        return 'Funny'


def inverso(s):
    inv_s = ''

    for i in range(len(s)-1, -1, -1):
        inv_s += s[i]
            
    return inv_s


main()