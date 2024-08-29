from aula_176_funcoes_de_primeira_classe import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f"Processando {titulo}")
    if callable(funcao):
        for i in lista:
            print(f"{1} => {funcao(i)}")


if __name__ == "__main__":
    processar("Dobros de 1 a 10", range(1, 11), dobro)
    print("-="*30)
    processar("Quadrado de 1 a 10", range(1, 11), quadrado)
