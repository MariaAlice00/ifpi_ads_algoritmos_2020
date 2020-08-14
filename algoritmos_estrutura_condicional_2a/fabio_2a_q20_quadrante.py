def main():
    angulo = int(input('Digite um ângulo entre  0° e 360°: '))
    quadrante(angulo)


def quadrante(angulo):
    if angulo >= 0 and angulo <= 90:
        print(f'{angulo} pertence ao primeiro quadrante')
    elif angulo > 90 and angulo <= 180:
        print(f'{angulo} pertence ao segundo quadrante')
    elif angulo > 180 and angulo <= 270:
        print(f'{angulo} pertence ao terceiro quadrante')
    else:
        print(f'{angulo} pertence ao quarto quadrante')


main()
