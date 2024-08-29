# print(dir(int))
# print("=" * 50)
# print(dir(float))

a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)
# Apartir que os cálculos tiverem um tipo float o resultado sempre vai ser folat, independentimento se o resultado for int
# ex:
# 1 + 1.0 = 2.0

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(3, 3))
print((-2).__abs__())  # função interna do INT
print(abs(-2))  # buildins
print((-3.6).__abs__())
