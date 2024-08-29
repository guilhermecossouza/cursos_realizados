# Aula 74 Validando argumento numérico
import math
import sys
import errno


def circulo(raio=0):
    return math.pi * raio ** 2


def help(nome_arquivo=""):
    print(
        f"É necessário informar o raio acima de 2.\nSintaxe {nome_arquivo} <raio>")


if __name__ == "__main__":
    caminho_arquivo = sys.argv[0].split("/")[-1]

    if len(sys.argv) < 2:
        help(caminho_arquivo)
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        help(caminho_arquivo)
        sys.exit(errno.EPERM)

    area = circulo(raio=float(sys.argv[1]))
    print(f"Área do circulo: {area}")
