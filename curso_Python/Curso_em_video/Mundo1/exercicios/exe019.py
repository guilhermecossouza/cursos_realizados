# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
from random import randint, choice
nomes = []
for c in range(1, 4):
    nomes.append(str(input("Digite o nome do aluno: ")))

print("O aluno que vai apagar o quadro é {}".format(nomes[randint(0, 3)]))
print("O aluno que vai apagar o quadro é {}".format(choice(nomes)))
