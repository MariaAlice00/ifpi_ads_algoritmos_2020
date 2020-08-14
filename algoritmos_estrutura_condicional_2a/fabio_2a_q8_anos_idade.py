import time

def main():
    print('Vamos calcular sua idade?')
    time.sleep(1)
    print('Começando com sua data de nascimento.')
    time.sleep(1)
    d_n = int(input('Dia que você nasceu? '))
    m_n = int(input('E o mês? '))
    a_n = int(input('E o ano? '))

    print('Agora, os dados do dia de hoje.')
    d_a = int(input('Que dia é hoje? '))
    m_a = int(input('E o mês? '))
    a_a = int(input('E o ano? '))

    idade(d_n, m_n, a_n, d_a, m_a, a_a)


def idade(d_n, m_n, a_n, d_a, m_a, a_a):
    idade_n = a_a - a_n
    if d_a > d_n and m_a >= m_n:
        print(f'Você tem {idade_n} anos!')
    elif d_a == d_n and m_a == m_n:
        print(f'Você tem {idade_n} anos, e está completando hoje. Parabéns!!!')
    else:
         idade_e = idade_n - 1
         print(f'Você tem {idade_e} anos!')


main()
