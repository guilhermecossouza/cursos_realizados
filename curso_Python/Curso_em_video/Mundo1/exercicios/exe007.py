# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nome = str(input("Digite o nome do aluno: "))
nota_um = float(input("Digite a primira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
media = (nota_um + nota_dois) / 2
print("O aluno {}, tevo as notas {}, {} e teve a média dê: {:.1f}".format(nome, nota_um, nota_dois, media))
