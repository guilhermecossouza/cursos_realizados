for c in range(1, 10):
    print(c)

print("-="*30)

cont = 1
while cont < 10:
    print(cont)
    cont += 1

print("-="*30)

n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("fim")

print("-="*30)

r = 'S'
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Deseja continuar [S/N]")).upper()
print("Fim")

print("-="*30)

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número:"))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("Você digitou {} números pares e {} núemros imapres.".format(par, impar))
