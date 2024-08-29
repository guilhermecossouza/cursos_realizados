# *args -> parâmetros posicionais (1, 2, 3, 4) -> criasse uma tupla
# **kwargs -> parâmentros nomeados ["n1": 1, "n2": 2] -> cria-se um dicionário
def todos_parametros(*args, **kwargs):
    print(f"*args = {args}")
    print(f"*kwargs = {kwargs}")


if __name__ == "__main__":
    print("-="*50)
    todos_parametros("a", "b", "c")  # -> parâmetros posicionais
    todos_parametros(nome="guilherme", idade=38)  # -> parâmetro nomeados
    todos_parametros(1, 2, 3, legal=True, valor=12.50)
    todos_parametros("Ana", False, [1, 2, 3], tamanho="M", fragil=False)
    # OBS: não pode colocar parametro posicionais depois do parametro nomenados -> erro
    # todos_parametros(nome="guilherme", idade=38, "casado") -> SyntaxError: positional argument follows keyword argument
    todos_parametros("casado", nome="guilherme", idade=38)
    print("-="*50)
