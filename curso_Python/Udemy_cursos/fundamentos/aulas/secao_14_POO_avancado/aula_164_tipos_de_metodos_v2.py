# método de instância recebi como primeiro parâmetro self
# método de classe recebi como primeiro parâmetro a classe ex: Humano
# método estático não recebe nenhum parâmetro

class Humano:
    # atributo de classe
    especie = "homo sapiens"  # atributo de classe

    def __init__(self, nome):
        self.nome = nome  # atributo que pertence a instância

    def das_cavernas(self):  # método de instância self como primeiro parâmentro
        self.especie = "homo neanderthalensis"  # atributo que pertence a instância
        return self

    @staticmethod
    def especies():
        adjetivos = ("Habilis", "Erectus", "Neanderthalensis", "Sapiens")
        return ("australopithecus", ) + tuple(f"Homo {adj}" for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


# sub classes
class Neanderthalensis(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = HomoSapiens("Jose")
    grokn = Neanderthalensis("Grokn")

    print(
        f"Evolução (a partir da classe): {', '.join(Neanderthalensis.especies())}")
    print(f"Evolução (a partir da instância): {', '.join(grokn.especies())}")
    print(f"Homo Sapiens  evoluido? {HomoSapiens.is_evoluido()}")
    print(f"Neandertal evoluido? {Neanderthalensis.is_evoluido()}")
    print(f"José evoluido: {jose.is_evoluido()}")
    print(f"Grokn evoluido: {grokn.is_evoluido()}")
