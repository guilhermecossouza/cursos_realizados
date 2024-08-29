frase = "Python é uma linguagem execelente"
# False -> Ptyhon é um linguaem Camel case , para ele letras maíusculas  e minúscula importam
print("py" in frase)
print("ing" in frase)  # True
print("py" not in frase)  # True
print(len(frase))
print(frase.lower())
# Faz uma cópia da variável frase adicionando as palavras em minúsculas, más a variável frase continua a mesma coisa
print("py" in frase.lower())
# Faz uma cópia da variável frase adicionando as palavras em maiúsculas, más a variável frase continua a mesma coisa
print(frase.upper())
print(dir(str))
help(str.center)
nome = "zaca"
print("-=" * 25)
print(nome.center(50))
print(len(nome.center(50)))

