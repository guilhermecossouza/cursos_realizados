# Sequencia fibonacci começa 0, 1 mais a soma do antecessor ex:
# 0 + 1 = 1 -> 1 + 1 -> 2 + 1 = 3, 3 + 2
# 0, 1, 1, 2, 3, 5, 8...

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=", ")
    contador = 0
    while True:
        proximo = ultimo + penultimo
        print(f"{proximo}", end=", ")
        penultimo = ultimo
        ultimo = proximo

        contador += 1
        if contador == 10:
            break


if __name__ == "__main__":
    fibonacci()
