# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 2 para hexadecimal

numero = int(input("Digite um número inteiro: "))
print("Qual a base de conversão deseja:\n 1 - para binário\n 2 - para octal\n 3 - para hexadecimal")
opcao = int(input("Opção: "))
if opcao == 1:
    print("O número {} para binário é: {}".format(numero, bin(numero)))
elif opcao == 2:
    print("O número {} para binário é: {}".format(numero, oct(numero)))
elif opcao == 3:
    print("O número {} para binário é: {}".format(numero, hex(numero)))
else:
    print("Opção desejada não existe!")


