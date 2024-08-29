# Escopo de variáveis
def teste():
    # para alterar a variavel local e não permitir que seja criada a função local digite global n
    # apartir desse monento a variavel global vai ser alterada
    # global n agora a variavel global vai passar a ser 10 e não 2
    n = 10  # Essa variável n não é a global, vai ser criada uma variável local onde n vale 8 e a global vale 5
    x = 8  # variável de escopo local, só vai funcionar dentro da função
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")


# programa principlal
if __name__ == "__main__":
    n = 2  # variável de global, vai funcinar eme todo em todo programa onde for passado
    print(f"No programa principla, n vale {n}")
    teste()
    # print(f"No programa principla, x vale {x}") #ERRO: variável de escopo local, só vai funcionar dentro da função
