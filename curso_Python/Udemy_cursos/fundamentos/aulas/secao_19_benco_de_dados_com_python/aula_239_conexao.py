# TRUSTED_CONNECTION -> Serve para fazer a autentificação usando o usuário do windows [Meu caso], recebe como valor string yes ou no
# Caso passe como yes não é necessário passar o login e senha do bando, caso no passar o login e senha
# driver caminhoa
# na busca do windows digitar Fontes de Dados ODBC
# video aula para conexao com sql server
# https://www.youtube.com/watch?v=PRWckK2NEaQ&t=50s

import pyodbc
_DRIVER = "SQL Server Native Client 11.0"
_SERVER = "DESKTOP-0I2D832"
_DATABASE = ""
_UID = None
_PWD = None
_TRUSTED_CONNECTION = "yes"
conexao = pyodbc.connect(
    f"DRIVER={_DRIVER};SERVER={_SERVER};DATABASE={_DATABASE};UID={_UID};PWD={_PWD};TRUSTED_CONNECTION={_TRUSTED_CONNECTION}"
)

print(conexao)
