'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''
# Minha resolução:

user = int(input(
    "Números de termos da sequência de Fibonacci que você deseja printar: \nfn = "))

prevfn = 0
fn = 1
nextfn = 0
index = 0

while index < user:
    prevfn = fn
    fn = nextfn
    nextfn = (fn + (prevfn))
    print("f{} = {}".format(index, fn))
    index += 1
print("Fim!")
