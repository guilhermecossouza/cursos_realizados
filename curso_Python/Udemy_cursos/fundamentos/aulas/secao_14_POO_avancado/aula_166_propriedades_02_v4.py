# método de instância recebi como primeiro parâmetro self
# método de classe recebi como primeiro parâmetro a classe ex: Humano
# método estático não recebe nenhum parâmetro

class Humano:
    # atributo de classe
    especie = "homo sapiens"  # atributo de classe

    def __init__(self, nome):
        self.nome = nome  # atributo que pertence a instância
        self._idade = None  # O UNDERLINE quer dizer o o atributo é privado da classe, más você pode acessa-lo normalmente, isso é so para meios de convenção

    @property
    def idade(self):  # este método é para a leitura do dados
        return self._idade

    @idade.setter
    def idade(self, idade):  # Esse método é para a validação do dado.
        if idade < 0:
            raise ValueError("Idade deve ser um número positivo")
        self._idade = idade

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
    jose.idade = 40
    print(f"Nome: {jose.nome} Idade: {jose.idade}")
    jose.idade = -40
    print(f"Nome: {jose.nome} Idade: {jose.idade}")
