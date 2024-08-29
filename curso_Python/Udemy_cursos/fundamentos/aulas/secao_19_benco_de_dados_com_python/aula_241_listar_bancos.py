from servisos import conexao_sql_server

conexao, cursor = conexao_sql_server.nova_conexao()
cursor.execute("SELECT name FROM sys.databases")

for i, banco in enumerate(cursor, start=1):
    print(f"baco de dados {i}: {banco[0]}")
