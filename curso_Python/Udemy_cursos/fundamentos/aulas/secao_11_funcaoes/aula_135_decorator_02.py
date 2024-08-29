def log(function):
    def decorator(*args, **kwargs):
        print(f"Início da chamado da função: {function.__name__}")
        print(f"{args}")
        print(f"{kwargs}")
        resultado = function(*args, **kwargs)
        print(f"Resultado da chamada: {resultado}")
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def subtracao(x, y):
    return x - y


if __name__ == "__main__":
    print(soma(5, 7))
    print(subtracao(5, y=7))
