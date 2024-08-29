# class Humano:
#     # atributo de classe
#     especie = "homo sapiens"  # atributo de classe

#     def __init__(self, nome):
#         self.nome = nome  # atributo que pertence a instância

#     def das_cavernas(self):
#         self.especie = "homo neanderthalensis"  # atributo que pertence a instância
#         return self  # retornando o objeto asssim posso acessar o objeto direto no método
#         # ex:
#         # a = Humano("zaca").das_cavernas()
#         # acessei o método sem precisar de mais linhas de código
#         # a = Humano("zaca")
#         # a.das_cavernas()
#         # saco?

# # pessoa = Humano("guilherme")
# # # o que vai prevalecer será o valor do atributo da classe R: homo sapiens
# # print(pessoa.especie)
# # pessoa.das_cavernas()
# # # o que vai prevalecer será o valor do atributo da instância R: homo neanderthalensis
# # print(pessoa.especie)


class Humano:
    # atributo de classe
    especie = "homo sapiens"  # atributo de classe

    def __init__(self, nome):
        self.nome = nome  # atributo que pertence a instância

    def das_cavernas(self):
        self.especie = "homo neanderthalensis"  # atributo que pertence a instância
        return self


if __name__ == "__main__":
    jose = Humano("José")
    grokn = Humano("Grokn").das_cavernas()
    print(f"Humano.especie: {Humano.especie}")
    print(f"jose.especie: {jose.especie}")
    print(f"grokn.especie: {grokn.especie}")
