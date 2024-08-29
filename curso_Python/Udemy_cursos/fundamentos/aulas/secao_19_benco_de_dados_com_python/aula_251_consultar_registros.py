from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

strSQL = "SELECT * FROM Contatos"
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(strSQL)
        dados = cursor.fetchall()
    except ProgrammingError as e:
        print(e.args)
    else:
        for contato in dados:
            print(f"contato: {contato[0]} telefone: {contato[1]}")
