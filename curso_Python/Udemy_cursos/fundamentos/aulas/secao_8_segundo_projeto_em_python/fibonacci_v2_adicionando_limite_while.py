# Sequencia fibonacci começa 0, 1 mais a soma do antecessor ex:
# 0 + 1 = 1 -> 1 + 1 -> 2 + 1 = 3, 3 + 2
# 0, 1, 1, 2, 3, 5, 8...

def fibonacci(limite=0):
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=", ")
    while ultimo < limite:
        proximo = ultimo + penultimo
        print(f"{proximo}", end=", ")
        penultimo = ultimo
        ultimo = proximo


if __name__ == "__main__":
    limite = int(input("limite para a sequência de fibonacci: "))
    fibonacci(limite)
