from aula_242_funcao_nova_conexao import nova_conexao
from pyodbc import ProgrammingError


tabela_contatos = """CREATE TABLE Contatos(nome VARCHAR(50), tel VARCHAR(40))"""

tabela_email = """CREATE TABLE Emails(Id int IDENTITY(1,1) PRIMARY KEY, Dono VARCHAR(50))"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_email)
    except ProgrammingError as e:
        print(e.args)
