# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

anos = int(input('Quantos anos você tem?: '))
meses = int(input('E meses?: '))
dias = int(input('E dias?: '))

ano = anos * 365
mes = meses * 30
resultado_dias = ano + mes + dias

print('{} anos {} meses e {} dias equivalem a {} dias'. format(anos, meses, dias, resultado_dias))
