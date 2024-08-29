def tag_bloco(texto, classe="success", inline=False):
    tag = "span" if inline is True else "div"
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tag_bloco("texto adicionado com sucesso", inline=True))
