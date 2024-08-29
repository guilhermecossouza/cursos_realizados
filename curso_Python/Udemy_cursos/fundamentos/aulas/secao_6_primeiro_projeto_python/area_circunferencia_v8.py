# Aula 67 Criando funcçõa sem retorno
import math


def circulo(raio=0):
    print(f"Área do circulo: {math.pi * raio ** 2}")


if __name__ == "__main__":
    raio = float(input("Informe o raio: "))
    circulo(raio)
