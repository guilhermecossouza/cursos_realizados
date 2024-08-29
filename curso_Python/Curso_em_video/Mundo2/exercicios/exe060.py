''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

num = int(input("Digite um número: "))
mult = 1
while num >= 1:
    mult *= num
    num -= 1
print("Fatorial de 5 é: {}".format(mult))
