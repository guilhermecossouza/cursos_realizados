# implementação simplificada do map

def mapear(funcao, lista):
    for n in lista:
        yield funcao(n)


if __name__ == "__main__":
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
