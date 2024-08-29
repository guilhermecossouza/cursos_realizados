with open("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))

if arquivo.closed:
    print("O Arquivo foi fechado diretamento pelo python")
