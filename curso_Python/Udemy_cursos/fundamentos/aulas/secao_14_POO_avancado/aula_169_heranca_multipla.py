class Animal:

    @property
    def capacidades(self):
        return ("dormir", "comer", "beber")


class Homen(Animal):

    @property
    def capacidades(self):
        return super().capacidades + ("amar", "falar", "estudar")


class Aranha(Animal):

    @property
    def capacidades(self):
        return super().capacidades + ("fazer teia", "andar pelas paredes")


class HomenAranha(Homen, Aranha):

    @property
    def capacidades(self):
        return super().capacidades + ("bater em bandidos", "atirar teias")


if __name__ == "__main__":
    john = Homen()
    print(f"john: {john.capacidades}")

    aranha = Aranha()
    print(f"Aranha: {aranha.capacidades}")

    piter = HomenAranha()
    print(f"Homen aranha: {piter.capacidades}")
