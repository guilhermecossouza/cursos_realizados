#função armazenada dentro de uamvariável é uam funcção de primeira classe.
#funcção que terorna uma outr a funcção é uma função de alta ordem
def multiplicar(x):
    def clacular(y):
        return x * y
    return clacular


if __name__ == "__main__":
    # passando o x para a funcção que vai me retornar a funcao calcular
    dobro = multiplicar(2)
    # passando o x para a funcção que vai me retornar a funcao calcular
    tripulo = multiplicar(3)

    # OBS:
    # As variáveis dobro e tripulo se tornaram a funçao calcular
    print(dobro)
    print(tripulo)
    print(f"O dobro de 7 é {dobro(7)}")
    print(f"O tripulo de 3 é {tripulo(3)}")
