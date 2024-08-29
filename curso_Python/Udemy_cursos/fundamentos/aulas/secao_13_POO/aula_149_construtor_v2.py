# O construtor da classe que é o methodo __init__ e chamado na instancia do objeto
# ex:
# d1 = Data()

class Data:
    def __init__(self, dia=1, mes=1, ano=1970) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data(28, 2, ano="1982")
d1.dia = 28
d1.mes = 2
# d1.ano = 1984

print(d1.__str__())
