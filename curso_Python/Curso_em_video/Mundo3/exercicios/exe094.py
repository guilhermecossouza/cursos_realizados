"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""
pessoa = dict()
pessoas = list()
so_mulheres = list()
while True:
    opcao = str(input("Deseja realizar o cadastro [S/N]: ")).strip().upper()[:1]
    match opcao:
        case "S":
            pessoa["nome"] = str(input("Informe o nome: "))
            pessoa["sexo"] = str(input("Informe o sexo: ")).upper().strip()[:1]
            if pessoa["sexo"] == "F":
                so_mulheres.append(pessoa["nome"])
            pessoa["idade"] = int(input("Informe a sua idade: "))     
            pessoas.append(pessoa.copy())         
        case "N":
            break
print(f"Foram um total de {len(pessoas)} pessoas cadastradas.")
total_idade = 0
for dados in pessoas:
    total_idade += dados["idade"]

media = total_idade / len(pessoas)
pessoas.append(media)
print(pessoas)
print(f"A média de idade do grupo é: {pessoas[len(pessoas) - 1]}")
print(f"Nome da mulhered: {so_mulheres}")

  

