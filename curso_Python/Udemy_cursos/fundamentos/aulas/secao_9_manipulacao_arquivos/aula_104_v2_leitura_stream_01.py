# leitura stream é uma leitura por partes.
# videos e string são enviados para seu pc em partes.

arquivo = open(
    "./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv")
for registro in arquivo:
    print("Nome: {}, Idade: {}".format(*registro.split(",")))

arquivo.close()
