# Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, 
# escrevendo o resultado em forma de fração.

num_1 = int(input('Digite o numerador da primeira fração: '))
den_1 = int(input('Digite o denominador da primeira fração: '))
num_2 = int(input('Digite o numerador da segunda fração: '))
den_2 = int(input('Digite o denominador da segunda fração: '))

den_final = den_1 * den_2
num_final = (den_final // den_1 * num_1) + (den_final // den_2 * num_2)

print(f'A soma é {num_final}/{den_final}')
