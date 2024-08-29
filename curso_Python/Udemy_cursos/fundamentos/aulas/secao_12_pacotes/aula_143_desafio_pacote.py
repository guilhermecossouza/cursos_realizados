from app.utilitarios.gerador import novo_nome, nomes
from app.negocio import nome_existe
from app.negocio.backend import add_nome


if __name__ == "__main__":
    while True:
        nome = "zaca"
        if not nome_existe(nome, nomes()):
            add_nome(nome)
            break
print(nomes())
