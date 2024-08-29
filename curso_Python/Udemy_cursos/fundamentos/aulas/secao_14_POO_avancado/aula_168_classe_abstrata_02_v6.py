from abc import ABCMeta, abstractproperty
# Ao adicionar a calsse como uma classe abstrata ela não podereá ser instanciada exe: a baixo


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = "homo sapiens"  # atributo de classe

    def __init__(self, nome):
        self.nome = nome  # atributo que pertence a instância
        self._idade = None  # O UNDERLINE quer dizer o o atributo é privado da classe, más você pode acessa-lo normalmente, isso é so para meios de convenção

    @abstractproperty
    def inteligente(self):
        pass

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
class Neandertal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == "__main__":
    # anonimo = Humano("John Doe") erro: TypeError

    try:
        anonimo = Humano("John Doe")
        print(anonimo.inteligente)
    except TypeError:
        print("classe é abstrata abstrata")

    jose = HomoSapiens("Jose")
    print("{} da classe {}, inteligente: {}".format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    grogn = Neandertal("Grogn")
    print("{} da classe {}, inteligente: {}".format(
        grogn.nome, grogn.__class__.__name__, grogn.inteligente))
