def executar(funcao):
    if callable(funcao):  # Verifica se é uma função chamavel
        funcao()
    else:
        print(f"Não existe a função {funcao}")


def bom_dia():
    print("Bom dia!")


def bom_tarde():
    print("Bom tarde!")


if __name__ == "__main__":
    executar(bom_dia)
    executar(bom_tarde)
    executar(1)  # Erro não existe a funcção 1
