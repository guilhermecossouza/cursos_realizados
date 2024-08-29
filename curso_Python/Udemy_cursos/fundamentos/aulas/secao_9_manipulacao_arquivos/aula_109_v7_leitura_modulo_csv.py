# o python já tem uma biblioteca para trabalhar com arquivos csv
import csv


with open("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv") as arquivo:
    for pessoa in csv.reader(arquivo):
        print("Nome: {}, Idade: {}".format(*pessoa))
