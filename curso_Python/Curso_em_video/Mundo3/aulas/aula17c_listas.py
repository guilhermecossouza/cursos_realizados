a = [2, 3, 4, 7]
# Nesse momento a lista b é uma cópia de a ou seja o python cria uma ligação entre elas
# ou seja se alterar uma altera as duas
b = a
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print("-="*30)
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print("-="*30)
c = a[:]  # Em faliamento -> Nesse caso está passando os valors de a para b
c[3] = 0
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")
print("-="*30)
d = a.copy()  # podemos usar també a função copy
d[0] = 55
print(f"Lista D: {d}")
