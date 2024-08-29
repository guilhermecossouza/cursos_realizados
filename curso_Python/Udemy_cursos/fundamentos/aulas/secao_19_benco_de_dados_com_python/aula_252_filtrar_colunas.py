from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError

strSQL = "SELECT tel, nome FROM Contatos"
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(strSQL)
    except ProgrammingError as e:
        print(e.args)
    else:
        for contato in cursor:
            print('\t'.join(str(campo) for campo in contato))
