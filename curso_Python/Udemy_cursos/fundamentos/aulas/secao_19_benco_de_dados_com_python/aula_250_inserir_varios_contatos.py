# execute -> somente para um parãmetro
# executemany -> para vários parametrod
from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

with nova_conexao() as conexao:
    try:
        strSQL = "INSERT INTO Contatos(nome, tel) values(?, ?)"
        args = (("Gabriel", "992899599"), ("Hiago", "992899599"))
        cursor = conexao.cursor()
        cursor.executemany(strSQL, args)
        cursor.commit()
    except ProgrammingError as e:
        print(e.args)
    else:
        print(f"{cursor.rowcount} de registros")
