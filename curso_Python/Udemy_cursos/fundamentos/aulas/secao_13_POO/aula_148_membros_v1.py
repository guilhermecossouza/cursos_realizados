# OBS: todo métodoto de uma classe é obrigatório ter o self
# O self é a representação da classe instanciada no memento da execução

class Data:
    # def to_str(self):
    #     return f"{self.dia}/{self.mes}/{self.ano}"
    # esse método to_str ou seja converter para string pode ser substituido pelo médoto estpecial __str__
    # esse método é suportado por toso os objetos do python
    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.ano}"
    # nesse caso não é necessáro chamar a função


d1 = Data()
d1.dia = 28
d1.mes = 2
d1.ano = 2023

# print(f"{d1.dia}/{d1.mes}/{d1.ano}")
# print(f"{d1.to_str()}")
# Agora será opcional a chamada da função para que impima no console a data convertida em string
print(d1)


d2 = Data()
d2.dia = 17
d2.mes = 2
d2.ano = 2023
# print(d2.to_str())
# podendo ser chamada assim tambémfica mais claro no códio
print(d2.__str__())
