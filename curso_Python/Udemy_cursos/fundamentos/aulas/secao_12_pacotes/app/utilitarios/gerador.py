from random import randint


def nomes():
    return ["Guilherme", "Kenia", "Maria Vitória", "Hiago", "Gabriel"]


def novo_nome():
    return nomes()[randint(0, 4)]
