def tag(tag, *args, **kwargs):
    if "html_calss" in kwargs:
        kwargs["class"] = kwargs.pop("html_calss")
    atributos = " ".join(f'{chave}="{valor}"' for chave,
                         valor in kwargs.items())
    textos = "".join(args)
    return f"<{tag} {atributos}>{textos}</{tag}>"


if __name__ == "__main__":
    print(
        tag('p',
            tag('strong', 'Curso Python 3 por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Laitão', id='ll'),
            tag('span', '.'),
            html_calss='aleret')
    )
