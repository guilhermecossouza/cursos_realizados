# Aula 69 Obtendo Arguimento via terminal
import math
import sys


def circulo(raio=0):
    return math.pi * raio ** 2


if __name__ == "__main__":
    area = circulo(sys.argv[1])
    print(f"Área do circulo: {area}")
