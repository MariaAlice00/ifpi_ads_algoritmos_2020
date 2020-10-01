def main():
    menu = '##### Operações com Listas #####\n' \
    + '1 - Inserir novos valores\n' \
    + '2 - Mostrar valores em posição X\n' \
    + '3 - Mostrar todos os valores\n' \
    + '4 - Remover no Início\n' \
    + '5 - Remover no Final\n' \
    + '6 - Remover na Posição Específica\n' \
    + '7 - Inserir valores em Posição Específica\n' \
    + '8 - Qtd Pares\n' \
    + '9 - Qtd Ímpares\n' \
    + '10 - Qtd Primos\n' \
    + '11 - Qtd Positivos\n' \
    + '12 - Qtd Negativos\n' \
    + '13 - Qtd Zerados\n' \
    + '14 - Média dos Valores\n' \
    + '15 - Contar ocorrências de um dado valor\n' \
    + '16 - Dobrar todos os valores\n' \
    + '17 - Dobrar valores múltiplos de N\n' \
    + '18 - Apagar todos os valores\n' \
    + '0 - Sair\n' \
    + 'Digite uma opção: '

    opcao = int(input(menu))

    lista = []

    while opcao != 0:
        if opcao == 1: # Inserir novos valores 
            inserir_valores(lista)
        elif opcao == 2: # Mostrar valores em posição X
            mostrar_na_posicao(lista)
        elif opcao == 3: #Mostrar todos os valores
            print(lista)
        elif opcao == 4: # Remover no Início
            sem_inicio(lista)
        elif opcao == 5: # Remover no Final
            sem_fim(lista)
        elif opcao == 6: # Remover na Posição Específica
            sem_posicao_especifica(lista)
        elif opcao == 7: # Inserir valores em Posição Específica
            inserir_posicao_especifica(lista)
        elif opcao == 8: # Qtd Pares
            qtd_pares(lista)
        elif opcao == 9: # Qtd Ímpares
            qtd_impares(lista)
        elif opcao == 10: # Qtd Primos
            qtd_primos(lista)
        elif opcao == 11: # Qtd Positivos
            qtd_positivos(lista)
        elif opcao == 12: # Qtd Negativos
            qtd_negativos(lista)
        elif opcao == 13: # Qtd Zerados
            qtd_zerados(lista)
        elif opcao == 14: # Média dos Valores
            media(lista)
        elif opcao == 15: # Contar ocorrências de um dado valor
            ocorrencias(lista)
        elif opcao == 16: # Dobrar todos os valores
            dobrar_todos_valores(lista)
        elif opcao == 17: # Dobrar valores múltiplos de N
            dobrar_multiplos_especifico(lista)
        elif opcao == 18: # Apagar todos os valores
            apagar_todos_valores(lista)
        else:
            print('Opção inválida')

        input('<enter> para continuar...')
        opcao = int(input(menu))

    print('Fim da operação. Volte sempre!')


def inserir_valores(lista):
    qtd = int(input('Quantos valores você quer inserir? '))
        
    for q in range(qtd):
        valor = int(input())
        lista.append(valor)


def mostrar_na_posicao(lista):
    posicao = int(input('Posição desejada: '))
    
    print(lista[posicao])


def sem_inicio(lista):
    lista.pop(0)
    print(lista)


def sem_fim(lista):
    lista.pop()
    print(lista)


def sem_posicao_especifica(lista):
    posicao = int(input('Posição para remover: '))
    lista.pop(posicao)
    print(lista)    


def inserir_posicao_especifica(lista):
    posicao = int(input('Posição para inserir: '))
    valor = int(input('Valor inserido: '))

    lista.insert(posicao, valor)
    print(lista)


def qtd_pares(lista):
    pares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
    
    print('Existe(m) {} número(s) par(es)'.format(pares))


def qtd_impares(lista):
    impares = 0
    for num in lista:
        if num % 2 != 0:
            impares += 1
    
    print('Existe(m) {} número(s) ímpar(es)'.format(impares))


def qtd_primos(lista):
    primos = []
    for num in lista:
        if eh_primo(num) == True:
            primos.append(num)
    
    print('Existe(m) {} número(s) primo(s)'.format(len(primos)))
 

def eh_primo(num):
    cont = 0
    for c in range(1, num+1):
        if num % c == 0:
            cont += 1

    if cont == 2:
        return True
    else: 
        return False


def qtd_positivos(lista):
    positivos = 0
    for num in lista:
        if num > 0:
            positivos += 1
    
    print('Existe(m) {} número(s) positivo(s)'.format(positivos))


def qtd_negativos(lista):
    negativos = 0
    for num in lista:
        if num < 0:
            negativos += 1
    
    print('Existe(m) {} número(s) negativo(s)'.format(negativos))


def qtd_zerados(lista):
    zerados = 0
    for num in lista:
        if num == 0:
            zerados += 1
    
    print('Existe(m) {} número(s) zerado(s)'.format(zerados))


def media(lista):
    cont = 0
    soma = 0
    for num in lista:
        soma += num
        cont += 1

    media = soma / cont

    print('A média dos números é: {}'.format(media))


def ocorrencias(lista):
    valor_especifico = int(input('Qual valor você quer saber quantas vezes apareceu? '))
   
    ocorrencia = 0
    for num in lista:
        if num == valor_especifico:
            ocorrencia += 1

    print('O número {} apareceu {} vez(es)'.format(valor_especifico, ocorrencia))


def dobrar_todos_valores(lista):
    valores_dobrados = []
    for num in lista:
        num_vezes_dois = num * 2
        valores_dobrados.append(num_vezes_dois)
    
    print(valores_dobrados)


def dobrar_multiplos_especifico(lista):
    multiplo = int(input('Serão dobrados os valores múltiplos de qual número? '))

    c = 0
    for num in lista:
        if num % multiplo == 0:
            novo_valor = num * 2
            lista[c] = novo_valor            
 
        c += 1

    print(lista)


def apagar_todos_valores(lista):
    c = 0
    while len(lista) >= 1:
        for num in lista:
            lista.pop()
    
    print(lista)


main()
