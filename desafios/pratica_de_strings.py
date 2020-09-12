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


def eh_letra(m):
    return ord(m) >= 65 and ord(m) <= 90 or ord(m) >= 97 and ord(m) <= 122


def pass_dois(msg2):
    msg3 = pass_um(msg2)
    msg4 = ''

    for c in range(len(msg3)-1, -1, -1):
        msg4 += msg3[c]
            
    return msg4


def pass_tres(msg4):
    resto, msg7 = msg_a_transf(msg4)

    msg8 = resto + msg7

    return msg8


def sobra(msg4):
    msg5 = pass_dois(msg4)

    quant_msg4 = len(msg4) // 2
    primeiro = quant_msg4
    ultimo = len(msg4) - 1

    resto = ''
    for r in range(0, quant_msg4):
        resto += msg4[r]

    return primeiro, ultimo, resto


def msg_a_transf(msg4):
    primeiro, ultimo, resto = sobra(msg4)
    
    msg6 = ''
    for t in range(primeiro, ultimo+1):
        msg6 += msg4[t] 

    msg7 = ''
    for x in msg6:
        msg7 += chr(ord(x) - 1)

    return resto, msg7


main()
