from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

strSQL = "SELECT tel, nome FROM Contatos"
with nova_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(strSQL)
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
