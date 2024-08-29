import random


def imprimir(imp=True):
    if imp is True:
        print("ACERTOU")
    else:
        print("ERROU")


for numero in range(1, 7):
    if numero % 2 == 1:
        continue
    else:
        if numero == random.randint(1, 6):
            imprimir()
            break
        else:
            imprimir(False)
