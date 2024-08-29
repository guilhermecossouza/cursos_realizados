from aula_193_generators_01 import cores_arco_iris

def sequencia():
    inicio = 0
    while True:
        inicio += 1
        yield inicio
        

if __name__ == "__main__":
    sequencia_numerica = sequencia()
    
    print(next(sequencia_numerica))
    print(next(sequencia_numerica))
    print(next(sequencia_numerica))
    print(next(sequencia_numerica))
    print(next(sequencia_numerica))
    print(next(sequencia_numerica))