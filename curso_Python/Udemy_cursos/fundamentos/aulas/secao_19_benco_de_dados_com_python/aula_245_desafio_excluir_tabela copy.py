from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

with nova_conexao() as conexao:
    try:
        conexao.execute("DROP TABLE Emails")
    except ProcessLookupError as e:
        print(e.args)
