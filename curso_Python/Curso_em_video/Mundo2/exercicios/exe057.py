'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''
sexo = str(input("Informe o sexo [M ou m ou F ou f]: ")).strip()[:1]
while sexo not in "MmFf":
    sexo = str(input("Sexo informado incorretamente\nInforme o sexo [M ou m ou F ou f]: ")).strip()[:1]

print("Informação salva com sucesso:")
   

