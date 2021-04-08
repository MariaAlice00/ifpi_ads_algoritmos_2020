'''"
passadas" deve retornar a string tranformada. O print deve ficar sob responsabilidade apenas da main
msg2[::-1] --> faça seu inverter...
msg3[0:quant_msg3] --> faça seu substring
def eh_letra(m):    return m in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Ajuste seu eh_letra para verificar fica via ascii e nao assim com operador IN
Transforme cada passada numa função, assim vc poderá reutizar o código.
'''
 

def main():
    n = int(input())
    
    passadas(n)


def passadas(n):
    for c in range(0, n):
        msg1 = str(input())

        # passada 1
        msg2 = ''
        for m in msg1:
            if eh_letra(m):
                msg2 += chr(ord(m) + 3)
            else:
                msg2 += m

        # passada 2
        msg3 = msg2[::-1]

        # passada 3
        quant_msg3 = len(msg3) // 2
        primeiro = quant_msg3
        ultimo = len(msg3) - 1
        resto = msg3[0:quant_msg3]
        
        msg4 = msg3[primeiro:ultimo+1]

        msg5 = ''
        for x in msg4:
            msg5 += chr(ord(x) - 1)

        msg6 = resto + msg5

        print(msg6)


def eh_letra(m):
    return m in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


main()