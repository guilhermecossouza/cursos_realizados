# OBS: O range ignora o último valor
# range(1, 10) -> vai de 1 á 9

for i in range(1, 11):
    print("i = {}".format(i))

for j in range(10):  # informado um valor, por default ele vai iniciar do 0
    print(f"j = {j}")

for a in range(0, 11, 2):  # Podemos colocar salto de números
    print(f"Par = {a}")

# montado uma tabuada
print("-="*50)
for x in range(0, 11):
    for y in range(1, 11):
        print(f"{x} X {y} = {x * y}")
    print("")
