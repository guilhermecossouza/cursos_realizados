# Membros de instância VS membros estáticos

class Objeto:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


# para cadas instancia criada os valores pertencem a instancia
class Objeto2:
    ano = "2023"

    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes


# para cadas instancia criada os valores pertencem a instancia
data = Objeto(2, 7, 2023)  # atibuto de instância
data.dia = 10  # -> acessado m atributo pela instância data
data1 = Objeto(3, 10, 2024)  # atibuto de instância

# se o atributo pertence a classe ele dexa de ser pertencente a instância
# ano virou um membro estático
data2 = Objeto2(3, 10)  # atibuto de instância
# agora posso acessar o atributo ano de precisar de instanância
data2.ano = 20250
