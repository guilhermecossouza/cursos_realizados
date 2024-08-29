"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione tambeem as docstrings da função
"""

def notas(*args, situacao=False):
    """Função verifica:quantidade de notas
        a maior nota
        a menor nota
        a média da turma
        a situação (opcional)"""
    dados = dict()
    notas = args    
    media = 0
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    sorted(notas)
    dados["qtdNotas"] = len(notas)
    dados["maiorNota"] = notas[len(notas) - 1]
    dados["menorNota"] = notas[0]
    dados["media"] = f"{media:.1f}"

    if situacao is True:
        if media <= 5:
            dados["situacao"] = "ruim".upper()
        elif 5 < media < 8:
            dados["situacao"] = "bom".upper()
        else:
            dados["situacao"] = "ótimo".upper()
    return dados

dados = notas(5.5, 10, 10, situacao=True)
print(dados)
print("-="*30)
print(f"Quantidade de notas cadastrados: {dados['qtdNotas']}")
print(f"Maior nota: {dados['maiorNota']}")
print(f"Menor nota: {dados['menorNota']}")
print(f"Média aluno: {dados['media']}")
print(f"Situação aluno: {dados['situacao']}")
print("-="*30)
