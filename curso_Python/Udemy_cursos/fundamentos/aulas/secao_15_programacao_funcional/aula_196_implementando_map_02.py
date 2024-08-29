# implementação simplificada do map

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    # print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
