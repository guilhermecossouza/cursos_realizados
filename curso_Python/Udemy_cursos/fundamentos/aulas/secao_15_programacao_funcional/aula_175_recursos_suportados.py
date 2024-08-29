# leitura e entendimento apostila.

# função zip
# junta duas lista formando pares
# resultado é uma lista com dicionários com os pares dentro

nome = ["Pedro", "Ana", "José"]
sobre_nome = ["Silva", "Pereira", "Gonsalves"]
juntos = zip(nome, sobre_nome)
print(juntos)  # zip object at 0x0000024F7BD6E1C0

juntos = list(juntos)
# [('Pedro', 'Silva'), ('Ana', 'Pereira'), ('José', 'Gonsalves')]
print(juntos)

juntos = tuple(juntos)
print(juntos)  # (('Pedro', 'Silva'), ('Ana', 'Pereira'), ('José', 'Gonsalves'))

juntos = dict(juntos)
print(juntos)  # {'Pedro': 'Silva', 'Ana': 'Pereira', 'José': 'Gonsalves'}
