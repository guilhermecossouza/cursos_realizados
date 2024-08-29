"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente
"""
print("-=" * 20)
print("{:^40}".format("Boletim escolar"))
print("Cadastro aluno!")
print("-=" * 20)
lista = []
lista_cadastro = []
while True:
    opcao = str(input("Deseja cadastrar um aluno [S/N]: ")).strip().upper()[:1]
    match opcao:
        case "S":
            nome = str(input("Informe o nome do aluno: ")).strip().upper()
            nota_um = float(input("Informe a primeira nota do aluno: "))
            nota_dois = float(input("Informe a segunda nota do aluno: "))
            lista.append(nome)
            lista.append(nota_um)
            lista.append(nota_dois)            
        case "N":
            break
    lista_cadastro.append(lista)
    lista = []
media = 0
for indice, lista_aluno in enumerate(lista_cadastro):    
    media = (lista_aluno[1] + lista_aluno[2]) / 2
    lista_aluno.append(media)
    media = 0

for lista in lista_cadastro:
    print("-="*40)
    print(f"Nome: {lista[0]}")
    print(f"Nota 1: {lista[1]}")
    print(f"Nota 2: {lista[2]}")
    print(f"Média : {lista[3]}")

opcao = str(input("Deseja mostar as informações por aluno? [S/N]")).strip().upper()[:1]
match opcao:
    case "S":
        nome = str(input("Informe o nome do aluno: ")).strip().upper()
        for lista in lista_cadastro:
            if nome in lista:
                print(f"Nome: {lista[0]}")
                print(f"Nota 1: {lista[1]}")
                print(f"Nota 2: {lista[2]}")
                print(f"Média : {lista[3]}")                
    case "N":
        print("Obrigado pos usar o sistema cadastro aluno.")
    


