import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.datetime.now()

    def __str__(self) -> str:
        return f"{self.descricao} ({'Concluida' if self.feito is True else ''})"

    def concluir(self):
        self.feito = True


def main():
    casa = list()
    casa.append(Tarefa("Passar Roupa"))
    casa.append(Tarefa("Lavar pratos"))
    
    # list comprehension
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Lavar pratos"]

    for tarefa in casa:
        print(f" - {tarefa}")


if __name__ == "__main__":
    main()
