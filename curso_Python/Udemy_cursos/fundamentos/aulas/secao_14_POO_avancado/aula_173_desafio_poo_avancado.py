class ClasseSimples:
    contador = 0

    def __init__(self) -> None:
        # qualquer das duas fromas dariam certas
        # self.__class__.contador += 1
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == "__main__":
    lista = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)
