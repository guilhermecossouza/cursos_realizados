#-> VERSÃO MAIS ANTIGA E NÃO RECOMENDADA AO USO
#-> 1°
nome, idade = "Ana", 30
print("Nome %s, Idade %s" % (nome, idade))
nome, idade = "Ana", 30.98765
print("Nome %s, Idade %f" % (nome, idade)) #-> impressão de ponto flutuante
print("Nome %s, Idade %.2f" % (nome, idade)) #-> impressão de ponto flutuante , com duas casas decimais
print("Nome %s, Idade %.1f" % (nome, idade)) #-> impressão de ponto flutuante , com uma casas decimais

nome, idade = "Ana", 30
#podemos adicionar valores na impressão com %r
print("Nome %s, Idade %s %r, %r" % (nome, idade, True, False))
#podemos adicionar valores na impressão com %s
print("Nome %s, Idade %s %s, %s" % (nome, idade, True, False))
#podemos adicionar valores na impressão com %d -> converte valores booleanos para inteiros 1 ou 0
print("Nome %s, Idade %s %d, %d" % (nome, idade, True, False))

#-> 2°
nome, idade = "Ana", 30
print("Nome {0}, Idade {1}".format(nome, idade)) #-> para versões do Pyhon < 3.6

#-> 3°
#acima do Python 3.6
nome, idade = "Ana", 30
print(f"Nome {nome}, Idade {idade}")
#podemos adicionas expreções
print(f"Nome {nome}, Idade {idade} -> {2 ** 8 - 1}")
#-> 3°
#usando import string
from string import Template
s = Template("Nome: $nome Idade: $idade")
print(s.substitute(nome=nome, idade=idade))

