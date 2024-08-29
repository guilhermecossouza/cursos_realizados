# Para localizar arquivos
# import os
# for f in os.listdir("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv"):
#     print(f)
arquivo = open(
    "./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv")
dados_arquivo = arquivo.read()
arquivo.close()

for registro in dados_arquivo.splitlines():
    # print(*registro.split(",")) forma simple
    # print(f"Nome: {registro.split(',')[0]}, Idade: {registro.split(',')[1]}") usando f string
    # usando o recurso do asterisco
    print("Nome: {}, Idade: {}".format(*registro.split(",")))
