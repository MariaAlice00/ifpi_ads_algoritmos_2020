import os
import json

def main():
    celulares = inicializar('celulares.bd')

    menu = tela_principal()

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print('Novo celular')
            celular = {}
            novo_celular(celular)

            celulares.append(celular)
            print('Celular cadastrado!')

        elif opcao == 2:
            q = len(celulares)
            print('*********** Listando {} celular(es) ***********'.format(q))
        
            for celular in celulares:
                listando_celulares(celular)

        elif opcao == 3:
            nome = input('Digite o nome: ')

            celulares_encontrados_por_nome = buscar_celulares_por_nome(nome, celulares)

            for celular in celulares_encontrados_por_nome:
                print('=> {} - {}'.format(celular['nome'], celular['marca']))
                
        elif opcao == 4:
            marca = input('Digite a marca: ')

            celulares_encontrados_por_marca = buscar_celulares_por_marca(marca, celulares)

            for celular in celulares_encontrados_por_marca:
                print('=> {} - {}'.format(celular['nome'], celular['marca']))

        else: 
            print('Digite uma opção válida!')

        input('<enter> para continuar...')
        os.system('cls')
        opcao = int(input(menu))

    finalizar('celulares.bd', celulares)


def tela_principal():
    menu = '******* APP CELULARES *******\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Buscar celular por nome\n'
    menu += '4 - Buscar celular por marca\n'
    menu += '0 - Sair\n'
    menu += '\n>>> '

    return menu


def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo): # se o arquivo existir...
        arquivo = open(nome_arquivo, 'r')    
        dados = arquivo.readline() # em uma linha
        arquivo.close()
        celulares_carregados = json.loads(dados) # converter
    
    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares) # inverso de json.loads
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def novo_celular(celular):
    celular['nome'] = input('Nome: ')
    celular['marca'] = input('Marca: ')
    celular['tela'] = input('Tela: ')
    celular['valor'] = float(input('Valor: R$ '))
    celular['cam_front'] = input('Tem câmera frontal? (sim/nao): ')


def listando_celulares(celular):
    print('Nome:', celular['nome'])
    print('Marca:', celular['marca'])
    print('Tela:' , celular['tela'])
    print('Valor: R$', celular['valor'])
    print('Tem câmera frontal?', celular['cam_front'])
    print('*'*25)


def buscar_celulares_por_nome(nome, celulares):
    celulares_encontrados_por_nome = []
    for celular in celulares:
        if nome == celular['nome']:
            celulares_encontrados_por_nome.append(celular)

    return celulares_encontrados_por_nome


def buscar_celulares_por_marca(marca, celulares):
    celulares_encontrados_por_marca = []
    for celular in celulares:
        if marca == celular['marca']:
            celulares_encontrados_por_marca.append(celular)

    return celulares_encontrados_por_marca


def tela_celular_selecionado():
    opcoes = '1 - Mostrar detalhes\n'
    opcoes += '2 - Remover\n'
    opcoes += '3 - Editar\n'
    opcoes += '4 - Duplicar registro\n'
    opcoes += '\n>>> '

    return opcoes

main()