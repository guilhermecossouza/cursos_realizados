# Uma funcção pode ter outra função dentro dela o nome é inner function

def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)
print(soma_5(5))
print(soma(2, 3)(5))
