# Parâmetros opcionais
def soma(a=0, b=0, c=0):
    """A fnção executa a soma de matemática de três númeroa

    Args:
        a (int, optional): _description_. Defaults to 0.
        b (int, optional): _description_. Defaults to 0.
        c (int, optional): _description_. Defaults to 0.
    """
    s = a + b + c
    print(f"A soma vale {s}")


soma(1, 2, 3)
soma(1, 2)
soma()
help(soma)
