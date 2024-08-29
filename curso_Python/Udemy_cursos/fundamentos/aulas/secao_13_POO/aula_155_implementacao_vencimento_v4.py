import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self) -> str:
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)"

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        # list comprehesion
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel erro IndexErro
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.datetime.now()
        self.vencimento = vencimento

    def __str__(self) -> str:
        status = []
        if self.feito:
            status.append("(Concluida)")
        elif self.vencimento:
            if datetime.datetime.now() > self.vencimento:
                status.append("(Vencida)")
            else:
                dias = (self.vencimento - datetime.datetime.now()).days
                status.append(f"Vence em {dias} dias.")
        return f"{self.descricao} " + " ".join(status)

    def concluir(self):
        self.feito = True


def main():
    casa = Projeto("Tarefas de casa")
    casa.add("Passar roupas", datetime.datetime.now())
    casa.add("Lavar pratos")
    casa.add("Varrer casa", datetime.datetime.now() +
             datetime.timedelta(days=3, minutes=12))
    print(casa)
    casa.procurar("Lavar pratos").concluir()
    for tarefa in casa:
        print(f" - {tarefa}")
    print(casa)


if __name__ == "__main__":
    main()
