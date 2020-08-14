# Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

# Entrada
num_1 = float(input('Digite a primeira nota: '))
pes_1 = float(input('Digite o peso da primeira nota: '))
num_2 = float(input('Digite a segunda nota: '))
pes_2 = float(input('Digite o peso da segunda nota: '))
num_3 = float(input('Digite a terceira nota: '))
pes_3 = float(input('Digite o peso da terceira nota: '))

# Processamento
nota_1 = num_1 * pes_1
nota_2 = num_2 * pes_2
nota_3 = num_3 * pes_3
soma_1 = nota_1 + nota_2 + nota_3
soma_2 = pes_1 + pes_2 +pes_3
media = soma_1 / soma_2

# Saída
print('MÉDIA PONDERADA = {:.2f}'.format(media))