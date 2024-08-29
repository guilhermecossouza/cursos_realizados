# códigos repetitivos (ROTINA)
# a = 4
# b = 5
# s = a + b
# print(s)
# a = 8
# b = 9
# s = a + b
# print(s)
# a = 2
# b = 1
# s = a + b
# print(s)

def soma(a, b):
    print("A = {a} e B = {b}")
    s = a + b
    print(s)
    print("-="*30)


soma(4, 5)
soma(8, 9)
soma(2, 1)
# soma(4) #ERRO -> a função exige dois parametro (a, b)
soma(a=4, b=4)
soma(b=4, a=4)
