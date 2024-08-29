class HtmlToStringMixing:
    def __str__(self):
        html = super().__str__().replace("(", "<strong>(").replace(")", ")</strong>")
        return f" <span>{html}</span>"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self) -> str:
        return self.nome + "(pet)" if self.pet is True else ""


class PessoaHtml(HtmlToStringMixing, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixing, Animal):
    pass


if __name__ == "__main__":
    p1 = Pessoa("Maria Eduarda")
    print(p1)

    p2 = PessoaHtml("Roberto Carlos")
    print(p2)

    c1 = AnimalHtml("Chico")
    print(c1)
