from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

strSQL = "ALTER TABLE Contatos ADD Id INT IDENTITY(1,1)"
with nova_conexao() as connect:
    try:
        cursor = connect.cursor()
        cursor.execute(strSQL)
        cursor.commit()
    except ProcessLookupError as e:
        print(e.args)
