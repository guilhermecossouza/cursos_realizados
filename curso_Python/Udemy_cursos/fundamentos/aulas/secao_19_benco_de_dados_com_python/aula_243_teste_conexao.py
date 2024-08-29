from aula_242_funcao_nova_conexao import nova_conexao

with nova_conexao() as conexao:
    if conexao:
        print("Conectado!")

print("fim")
