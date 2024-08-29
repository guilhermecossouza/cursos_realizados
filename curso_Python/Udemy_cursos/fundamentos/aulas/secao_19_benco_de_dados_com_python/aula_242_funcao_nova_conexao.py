from contextlib import contextmanager
from pyodbc import connect

_DRIVER = "SQL Server Native Client 11.0"
_SERVER = "DESKTOP-0I2D832"
_DATABASE = "Agenda"
_UID = None
_PWD = None
_TRUSTED_CONNECTION = "yes"


@contextmanager
def nova_conexao():
    conexao = connect(
        f"DRIVER={_DRIVER};SERVER={_SERVER};DATABASE={_DATABASE};UID={_UID};PWD={_PWD};TRUSTED_CONNECTION={_TRUSTED_CONNECTION}"
    )

    try:
        yield conexao
    finally:
        if conexao:
            conexao.close()
