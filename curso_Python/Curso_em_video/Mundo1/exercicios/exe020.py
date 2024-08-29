# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

nomes = []
for c in range(0, 4):
    nomes.append(str(input("Digite o nome do aluno: ")))

shuffle(nomes)

print(nomes)
for p, nome in enumerate(nomes):
    print("Em posição {}° foi sorteado o aluno(a): {}".format((p + 1), nome))
