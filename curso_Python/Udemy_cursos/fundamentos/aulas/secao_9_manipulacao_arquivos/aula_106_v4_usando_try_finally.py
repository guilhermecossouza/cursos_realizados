
# Tratamento de erro
# este bloco a baixo está com erro:
# arquivo = open("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv")
# for registro in arquivo:
#     print("Nome: {}, Idade: {}".format(registro.strip().split(",")))
# arquivo.close()
# para tratar o erro usamos o try except finally

# Este bloco está ainda com erro
try:
    arquivo = open(
        "./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv")
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(registro.strip().split(',')))
finally:
    print("Dando erro ou não esse bloco vai ser sempre executado.")
    arquivo.close()
