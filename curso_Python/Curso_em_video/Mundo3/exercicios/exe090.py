"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno["nome"] = str(input("Nome aluno: ")).upper().strip()
aluno["media"] = float(input("Média do aluno: "))

if aluno["media"] >= 6:
    aluno["situacao"] = "APROVADO"
else:
    aluno["situacao"] = "REPROVADO"

print(f"Nome do aluno: {aluno['nome']}")
print(f"Média do aluno: {aluno['media']}")
print(f"Situação do aluno é {aluno['situacao']}")