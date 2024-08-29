import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self) -> str:
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)"

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        # list comprehesion
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel erro IndexErro
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.datetime.now()

    def __str__(self) -> str:
        return self.descricao + (" (Concluida)" if self.feito is True else '')

    def concluir(self):
        self.feito = True


def main():
    casa = Projeto("Tarefas de casa")
    casa.add("Passar roupas")
    casa.add("Lavar pratos")
    print(casa)
    casa.procurar("Lavar pratos").concluir()
    for tarefa in casa:
        print(f" - {tarefa}")
    print(casa)

    print("-=-"*50)
    mercado = Projeto("Compras no mercado")
    mercado.add("Frutas secas")
    mercado.add("Carne")
    mercado.add("Tomate")
    print(mercado)
    mercado.procurar("Carne").concluir()
    for tarefas in mercado:
        print(f" - {tarefas}")
    print(mercado)


if __name__ == "__main__":
    main()
