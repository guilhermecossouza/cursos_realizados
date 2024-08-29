from decimal import Decimal, getcontext
# print(1.1 + 2.2)  # resultado = 3.3000000000000003
print(Decimal(1) / Decimal(7)) # resultado = 0.1428571428571428571428571429
getcontext().prec = 4 # dico que para o calculo quero um precisaõ de 4 casas decimais
print(Decimal(1) / Decimal(7)) # resultado = 0.1429
getcontext().prec = 1
print(Decimal(1) / Decimal(7)) #resultado = 0.1
print(dir(Decimal))
