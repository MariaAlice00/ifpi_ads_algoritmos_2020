# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
# O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias?

desconto = 0.4 * 24.95
capa_com_desconto = 24.95 - desconto
capa = capa_com_desconto * 60

transporte = 3 + 0.75 * 59

custo_total = capa + transporte
custo_total = round(custo_total, 2)

print(f'O resultado é R$ {custo_total}')
