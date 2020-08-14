# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro)
# e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

hora_inicial = (6 * 3600) + (52 * 60)

trajeto_1 = 8 * 60 + 15
trajeto_2 = 3 * (7 * 60 + 12)
trajeto_3 = trajeto_1

hora = hora_inicial + trajeto_1 + trajeto_2 + trajeto_3

hora_final = hora // 3600
minuto_1 = hora % 3600
minuto_2 = minuto_1 // 60
segundo = minuto_1 % 60

print(f'O resultado é {hora_final} horas {minuto_2} minutos e {segundo} segundos')

