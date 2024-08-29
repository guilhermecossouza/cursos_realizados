# Docstring
def contador(i, f, p):
    """_Realiza um contador_

    Args:
        i (_int_): Ínicio da contagem
        f (_int_): FIm da contagem
        p (_inr_): passo ou pula
        OBS: Não possui retorno
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("fim")


# contador(2, 10, 2)
help(contador)
