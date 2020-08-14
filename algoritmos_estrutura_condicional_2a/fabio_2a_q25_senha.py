def main():
    senha = int(input('Digite a senha: '))
    senha_valida(senha)


def senha_valida(senha):
    if senha == 1234:
        print('ACESSO PERMITIDO')
    else:
        print('ACESSO NEGADO')


main()