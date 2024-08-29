''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''
soma_idade = 0
nome_pessoa_mais_velha = ""
qtd_mulheres = 0
for contador in range(3):
    nome = str(input("Informe o seu nome: "))
    idade = int(input("Informe a sua idade: "))
    sexo = str(input("Informe o sexo: ")).upper().strip()[:1]

    soma_idade += idade

    if contador == 0:
        idade_maior = idade
        nome_pessoa_mais_velha = nome
    else:
        if idade > idade_maior:
            idade_maior = idade
            nome_pessoa_mais_velha = nome
    if sexo == "F":
        if idade < 20:
            qtd_mulheres += 1

print("Média de idade é {} anos".format((soma_idade / 3)))
print("Nome da pessoa mais velha: {}".format(nome_pessoa_mais_velha))
print("{} mulheres tem meno de 20 anos de idade".format(qtd_mulheres))
