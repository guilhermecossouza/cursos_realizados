from aula_242_funcao_nova_conexao import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM information_schema.tables;")
    for i, tb in enumerate(cursor, start=1):
        print(f"Nome banco: {tb[0]}, nome tabela: {tb[2]}")
