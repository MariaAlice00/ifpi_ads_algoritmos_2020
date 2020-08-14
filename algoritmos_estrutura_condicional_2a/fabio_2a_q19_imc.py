def main():
    altura = float(input('Altura em metros: '))
    peso = float(input('Peso em quilogramas: '))
    imc(altura, peso)


def imc(altura, peso):
    imc = peso / (altura ** 2)
    if imc < 25:
        print('Com {:.2f} de IMC, você está com o peso NORMAL!'.format(imc))
    elif imc >= 25 and imc <= 30:
        print('Com {:.2f} de IMC, você está OBESO!'.format(imc))
    else:
        print('Com {:.2f} de IMC, você está com OBESIDADE MÓRBIDA!'.format(imc))


main()

