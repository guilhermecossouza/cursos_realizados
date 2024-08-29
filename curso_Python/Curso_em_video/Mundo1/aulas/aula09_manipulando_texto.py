frase = "Curso em Video Python"
# Fatiamento de string
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Alalise de string

# vai mostrar a quantidade de caracters [ conta os espações em branco ]
print(len(frase))
# vai relizar uma contagem de quantos caracters tem usando o parametro nos caso a baixo 3
print(frase.count("o"))
# a mesma coisa do de cima na busca e contagem do caracter MAS vai da posição 0 á posição 13 [ignora o último caracter]
print(frase.count("o", 0, 13))
# vai realizar uma busca na frase e retornar a posição inicial onde ele achou, caso ele não ache ele retorna -1
print(frase.find("deo"))
print(frase.find("@"))

# verifica se existe um palavra dentro da frase [se exitir retorna True se não False
print("Curso" in frase)  # operador
print("Carro" in frase)  # operador

# transformação
print(frase.replace("Python", "Android"))
print(frase.upper())  # vai passar tudo para maiúsculo
print(frase.lower())  # vai passar tudo para minúscula
# vai pasar o primeiro caracter para maiúscula e o resto minuscula
print(frase.capitalize())
# vai passar o promiro caracter de cara palavra para maiúscula e o resto minucula
print(frase.title())

frase = "   Aprenda Python   "
print(frase)
print(frase.strip())  # vai remover os espaços a direita e a esquerda da frase
print(frase.rstrip())  # vai remover os espações a direita
print(frase.lstrip())  # vai remover os espações a esquerda

# divisão de string
frase = "Curso em Video Python"
print(frase.split())

# junção
print("".join(frase.split()))
print(" - ".join(frase.split()))
print(" ".join(frase.split()))
