# OBS: Atenção máxima para a condição  de parada, essa condição não informada vai gerar um erro no python
# A funcção recursiva e quando afunção chama ela mesma
def imprimir(maximo, atual):
    if atual >= maximo:
        return
    else:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(10, 1)
