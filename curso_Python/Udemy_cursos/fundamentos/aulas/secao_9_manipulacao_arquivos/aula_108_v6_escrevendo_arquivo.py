with open("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.csv") as arquivo:
    # Aqui ele irá criar um novo arquivo e esrever nele
    with open("./curso_udemy/fundamentos/aulas/secao_9_manipulacao_arquivos/pessoas.txt", "w") as entrada:
        for registro in arquivo:
            pessoa = "Nome: {}, Idade: {}".format(*registro.strip().split(","))
            print(pessoa, file=entrada)

if arquivo.closed:
    print("Arquivo fechado")

if entrada.closed:
    print("Arquivo fechado")
