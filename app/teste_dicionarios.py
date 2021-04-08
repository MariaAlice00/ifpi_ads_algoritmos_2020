import os

def main():
    menu = '** Países **\n'
    menu += '1 - add\n'
    menu += '2 - list\n'
    menu += '3 - search\n'
    menu += '0 - quit\n'
    menu += '\n>>> '

    opcao = int(input(menu))

    paises = []

    while opcao != 0:
        if opcao == 1:
            pais = {}
            pais['nome'] = input('Nome: ')
            pais['continente'] = input('Continente: ')
            pais['populacao'] = obter_inteiro_positivo('População (M): ') # validar dados

            paises.append(pais)
        
        elif opcao == 2:
            print('Lista de países')
            for pais in paises:
                mostrar_paises(pais)

        elif opcao == 3:
            busca = input('Digite o continente: ')
            
            paises_encontrados = pesquisar_por_continente(paises, busca)

            for pais in paises_encontrados:
                mostrar_paises(pais)

        else:
            print('Opção inválida')
        
        input('<enter>...')
        os.system('cls')
        opcao = int(input(menu))


def mostrar_paises(pais):
    print('Nome:', pais['nome'])
    print('Continente:', pais['continente'])
    print('População (M):', pais['populacao'])
    print('--------------------------------')


def pesquisar_por_continente(paises, busca):
    paises_encontrados = []
    for pais in paises:
        if busca in pais['continente']:
            paises_encontrados.append(pais)

    return paises_encontrados


def obter_inteiro_positivo(msg):
    valor = obter_inteiro(msg)

    while valor <= 0:
        print('Você deve digitar um número positivo')
        valor = obter_inteiro(msg)

    return valor
    

def obter_inteiro(msg):
    try:
        valor = int(input(msg))
        return valor
    except: 
        print('Valor inválido!')
        return obter_inteiro(msg)


main()