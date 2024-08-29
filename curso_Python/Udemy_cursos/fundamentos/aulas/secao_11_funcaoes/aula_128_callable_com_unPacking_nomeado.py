def calculo_preco_final(preco_bruto, calculo_imposto, **parametros):
    return preco_bruto + preco_bruto * calculo_imposto(**parametros)


def imposto_x(importado):
    return 0.22 if importado is True else 0


def imposto_Y(explosivo, fator_multiplicacao=1):
    return 0.11 * fator_multiplicacao if explosivo is True else 0


if __name__ == "__main__":
    preco_bruto = 134.98
    preco_final = calculo_preco_final(preco_bruto, imposto_x, importado=True)
    preco_final = calculo_preco_final(
        preco_final, imposto_Y, explosivo=True, fator_multiplicacao=1.5)
    print(f"Preço fianl R$ {preco_final :.2f}")
