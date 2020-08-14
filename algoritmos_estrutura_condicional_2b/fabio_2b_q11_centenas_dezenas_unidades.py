def main():
    num = int(input('Digite um número inteiro menor que 1000: '))
    num_str = str(num)
    quant_num = len(num_str)

    print(centena_dezena_unidade(quant_num, num))

   
def centena(num):
    return num // 100 % 10


def dezena(num):
    return num // 10 % 10
    

def unidade(num):
    return num // 1 % 10
    

def centena_dezena_unidade(quant_num, num):
    if quant_num == 3:
        if centena(num) == 1 and dezena(num) == 1 and unidade(num) == 1:
            return f'{centena(num)} centena, {dezena(num)} dezena e {unidade(num)} unidade.'
        elif centena(num) == 1 and dezena(num) == 1 and unidade(num) != 1:
            return f'{centena(num)} centena, {dezena(num)} dezena e {unidade(num)} unidades.'
        elif centena(num) == 1 and dezena(num) != 1 and unidade(num) == 1:
            return f'{centena(num)} centena, {dezena(num)} dezenas e {unidade(num)} unidade.'
        elif centena(num) != 1 and dezena(num) == 1 and unidade(num) != 1:
            return f'{centena(num)} centenas, {dezena(num)} dezena e {unidade(num)} unidade.'
        elif centena(num) != 1 and dezena(num) != 1 and unidade(num) != 1:
            return f'{centena(num)} centenas, {dezena(num)} dezenas e {unidade(num)} unidades.'
        elif centena(num) != 1 and dezena(num) != 1 and unidade(num) == 1:
            return f'{centena(num)} centenas, {dezena(num)} dezenas e {unidade(num)} unidade.'
        elif centena(num) != 1 and dezena(num) == 1 and unidade(num) != 1:
            return f'{centena(num)} centenas, {dezena(num)} dezena e {unidade(num)} unidades.'
        elif centena(num) == 1 and dezena(num) != 1 and unidade(num) != 1:
            return f'{centena(num)} centena, {dezena(num)} dezenas e {unidade(num)} unidades.'

    elif quant_num == 2:
        if dezena(num) == 1 and unidade(num) != 1:
            return f'{dezena(num)} dezena e {unidade(num)} unidades.'
        elif dezena(num) != 1 and unidade(num) == 1:
            return f'{dezena(num)} dezenas e {unidade(num)} unidade.'
        elif dezena(num) == 1 and unidade(num) == 1:
            return f'{dezena(num)} dezena e {unidade(num)} unidade.'
        elif dezena(num) != 1 and unidade(num) != 1:
            return f'{dezena(num)} dezenas e {unidade(num)} unidades.'
    
    elif quant_num == 1:
        if unidade(num) == 1:
            return f'{unidade(num)} unidade.'
        elif unidade(num) != 1:
            return f'{unidade(num)} unidades.'


main()

