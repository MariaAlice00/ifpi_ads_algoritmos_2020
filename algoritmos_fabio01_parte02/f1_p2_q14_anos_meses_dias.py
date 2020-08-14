# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

idade = int(input('Qual a sua idade em dias?: '))

ano = idade // 365
mes_1 = idade % 365
mes_2 = mes_1 // 30
dias = mes_1 % 30

print('{} dias equivalem a {} anos {} meses e {} dias'. format(idade, ano, mes_2, dias))