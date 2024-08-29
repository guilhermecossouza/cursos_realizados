import pyodbc

_DRIVER = "SQL Server Native Client 11.0"
_SERVER = "DESKTOP-0I2D832"
_DATABASE = ""
_UID = None
_PWD = None
_TRUSTED_CONNECTION = "yes"


def nova_conexao():
    conexao = pyodbc.connect(
        f"DRIVER={_DRIVER};SERVER={_SERVER};DATABASE={_DATABASE};UID={_UID};PWD={_PWD};TRUSTED_CONNECTION={_TRUSTED_CONNECTION}"
    )
    cursor = conexao.cursor()
    return conexao, cursor
