def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):  # o famoso *args -> vai receber um tupla
    soma = 0
    for numro in numeros:
        soma += numro
    return soma


if __name__ == "__main__":
    print(soma_2(3, 2))
    print(soma_3(2, 4, 6))
    print(soma_n(1))
    print("-=" * 30)
    print("Packing")
    # Packing => Eles está empacotando
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1, 1, 1))

    print("-=" * 30)
    print("Unpacking")
    # Unpacking => agora ele vai desempacotar e atribuir aos valores aos parametro
    tupla_numeros = (1, 2, 3)
    print(soma_3(*tupla_numeros))

    lista_numeros = [1, 2, 3]
    print(soma_3(*lista_numeros))
