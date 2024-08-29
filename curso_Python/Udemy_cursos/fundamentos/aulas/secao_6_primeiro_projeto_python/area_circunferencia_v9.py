# Aula 68 Adicionando retorno a funcção
import math


def circulo(raio=0):
    return math.pi * raio ** 2


if __name__ == "__main__":
    raio = float(input("Informe o raio: "))
    area = circulo(raio)
    print(f"Área do circulo: {area}")
