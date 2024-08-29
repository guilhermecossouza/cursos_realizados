import math
import random
# from math import sqrt, ceil, floor
# num = int(input("Digite um número: "))
num = random.randint(1, 100)
raiz = math.sqrt(num)
print("A raiz de {} é {:.2f}".format(num, raiz))
# ceil -> arrenonda para cima
print("A raiz de {} é {}".format(num, math.ceil(raiz)))
# floor -> arredonda para baixo
print("A raiz de {} é {}".format(num, math.floor(raiz)))
