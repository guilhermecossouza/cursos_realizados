# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

#frase = str(input("Digite uma frase: "))
frase = "amo amar"
print("Na frase: {}.".format(frase))
print("A letra a aparece {} vezes".format(frase.count("a")))
print("A primeira letra a aparece na posição {}".format(frase.find("a")))
print("A ultima letra a aparece na posição {}".format(frase.rfind("a")))

