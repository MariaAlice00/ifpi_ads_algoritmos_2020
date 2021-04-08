'''1 - +3
   2 - reverter
   3 - metade final -1
   "passadas" deve retornar a string tranformada. O print deve ficar sob responsabilidade apenas da main
    msg2[::-1] --> faça seu inverter...
    msg3[0:quant_msg3] --> faça seu substring
    def eh_letra(m):    return m in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Ajuste seu eh_letra para verificar fica via ascii e nao assim com operador IN
    Transforme cada passada numa função, assim vc poderá reutizar o código.
'''

def main():
    n = int(input())

    for c in range(0, n):
        mensagem = str(input())

        mensagem_nova = passadas(mensagem)
        print(mensagem_nova)


def passadas(msg_nova):
    msg_um = pass_tres(pass_dois(msg_nova))

    return msg_um


def pass_um(msg):
    msg2 = ''
    for m in msg:
        if eh_letra(m):
            msg2 += chr(ord(m) + 3)
        else:
            msg2 += m
    
    return msg2    


def pass_dois(msg2):
    msg3 = pass_um(msg2)
    msg4 = ''

    for c in range(len(msg3)-1, -1, -1):
        msg4 += msg3[c]
            
    return msg4


def pass_tres(msg4):
    msg5 = pass_dois(msg4)

    quant_msg4 = len(msg4) // 2
    primeiro = quant_msg4
    ultimo = len(msg4) - 1
    resto = msg4[0:quant_msg4] # 
        
    msg5 = msg4[primeiro:ultimo+1] #

    msg6 = ''
    for x in msg5:
        msg6 += chr(ord(x) - 1)

    msg7 = resto + msg6

    return msg7



def eh_letra(m):
    return ord(m) >= 65 and ord(m) <= 90 or ord(m) >= 97 and ord(m) <= 122


main()