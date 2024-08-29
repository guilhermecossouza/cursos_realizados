# Aula 73 Saindo com erro
import math
import sys
import errno


def circulo(raio=0):
    return math.pi * raio ** 2


def help(nome_arquivo=""):
    print(
        f"É necessário informar o raio acima de 2.\nSintaxe {nome_arquivo} <raio>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        caminho_arquivo = sys.argv[0].split("/")[-1]
        help(caminho_arquivo)
        # sys.exit(1)
        sys.exit(errno.EPERM)
    area = circulo(raio=float(sys.argv[1]))
    print(f"Área do circulo: {area}")
