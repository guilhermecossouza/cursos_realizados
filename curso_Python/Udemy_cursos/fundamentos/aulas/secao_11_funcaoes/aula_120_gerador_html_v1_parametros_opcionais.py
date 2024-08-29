def tag_bloco(texto, classe="success"):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    # teste com (assetions)
    # assert => ele executa como um teste, ele vai testar a sua função e por defaut você passa o que espera de retorno
    # Ex:
    print(tag_bloco("texto adicionado com sucesso"))
    # Se não tiver nenhum retorno quer dizer que retornou True ou seja tudo certo
    assert tag_bloco(
        "texto adicionado com sucesso") == '<div class="success">texto adicionado com sucesso</div>'

    # Nessa caso a baixo retorna erro pois o que vc espera e diferente do que a função vai retornar
    # assert tag_bloco(
    #     "texto adicionado com sucesso") == '<div class="success">texto adicionado sem sucesso</div>'
