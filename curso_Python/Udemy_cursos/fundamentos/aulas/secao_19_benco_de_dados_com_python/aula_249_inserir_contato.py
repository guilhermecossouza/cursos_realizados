from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

with nova_conexao() as conexao:
    try:
        # strSQL = "INSERT INTO Contatos(nome, tel) values(?, ?)"
        # args = ("guilherme", "992899599",)
        cursor = conexao.cursor()
        cursor.execute(
            """INSERT INTO Contatos(nome, tel) values(?, ?)""", "guilherme", "992899599"
        )
        cursor.commit()
    except ProgrammingError as e:
        print(e.args)
