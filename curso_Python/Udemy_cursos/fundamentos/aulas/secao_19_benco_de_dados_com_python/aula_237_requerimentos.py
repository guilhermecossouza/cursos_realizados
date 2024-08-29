# para instalar o conector do sql server comando:
# pip install pyodbc

try:
    from pyodbc import connect
except ModuleNotFoundError:
    print("SQL Server não instalado")
else:
    print("SQL Server instalado")
