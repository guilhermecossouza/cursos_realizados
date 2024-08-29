def tag_bloco(conteudo, classe="success", inline=False):
    tag = "span" if inline is True else "div"
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = "".join((f"<li>{item}</li>" for item in itens))
    return f"<ul>{lista}</ul>"


if __name__ == "__main__":
    print(tag_bloco("texto adicionado com sucesso", inline=True))
    print(tag_lista(*["guilherme", "Kenia"]))  # Unpacking
    print(tag_bloco(tag_lista("Guilherme", "Kenia"), classe="info"))  # packing
