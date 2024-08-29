import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self) -> str:
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)"

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga do operado +=
    # projeto += tarefa
    # casa += ....
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get("vencimento", None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(
            tarefa, Tarefa) else self._add_nova_tarefa
        kwargs["vencimento"] = vencimento
        funcao_escolhida(tarefa, **kwargs)

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


class Tarefa_Recorrente(Tarefa):
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.datetime.now() + datetime.timedelta(self.dias)
        nova_tarefa = Tarefa_Recorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto("Tarefas de casa")
    casa.add("Passar roupas", datetime.datetime.now())
    casa.add("Lavar pratos")
    casa.add("Varrer casa", datetime.datetime.now() +
             datetime.timedelta(days=3, minutes=12))
    casa += Tarefa_Recorrente(
        "Trocar lençois", datetime.datetime.now(), 7)
    casa.procurar("Trocar lençois").concluir()

    print(casa)
    casa.procurar("Lavar pratos").concluir()
    for tarefa in casa:
        print(f" - {tarefa}")
    print(casa)


if __name__ == "__main__":
    main()
