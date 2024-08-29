# Aula 75 Melhorando a mensagem de erro
import math
import sys
import errno


ERRO = "\033[91m"
NORMAL = "\033[0m"


def circulo(raio=0):
    return math.pi * raio ** 2


def help(nome_arquivo=""):
    print(
        f"{ERRO}É necessário informar o raio acima de 2.\nSintaxe {nome_arquivo} <raio>{NORMAL}")


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
