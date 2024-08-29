# o problema de usae parametro mutáveis é que eles fical quardados em memódia e na medida que altera a função altera o espaço em memória
# ex:
# [0, 1, 1] 1849767055872 -> chamada da função sem parametro
# [0, 1, 1, 2] alterou noemalmente a chamada da função com parametro
# [0, 1, 1, 2, 3, 5] 1849767055872 cahamada da função sem paramatro, ou seja tinha que ocupar outro espaço na
# memoria e ter o mesni resultado do início
# más não ele alterou o esmo espaço em memoria com resultados divergentes do que se espera

def fibonacci(sequencia=[0, 1]):
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(fibonacci(restart), id(restart))
    assert restart == [0, 1, 1, 2, 3, 5]
