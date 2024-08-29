import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self) -> str:
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)"

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
    for tarefa in casa.tarefas:
        print(f" - {tarefa}")
    print(casa)



if __name__ == "__main__":
    main()
