''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

maior_idade = 0
qtd_homens = 0
mulheres_idade_menos_18_anos = 0
while True:    
    opcao = str(input("Deseja realizar o cadastro? [ S/N ] ")).upper().strip()[:1]
    match opcao:
        case "S":
            idade = int(input("Digite sua idade: "))
            sexo = str(input("Digite o seu sexo: [M/F]")).upper().strip()
            match sexo:
                case "M":
                    qtd_homens += 1
                case "F":
                    if idade < 18:
                        mulheres_idade_menos_18_anos += 1 
            if idade > 18:
                maior_idade += 1
        case "N":
            break

print(f"Foram um total de {maior_idade} pessoas com mais de 18 anos.")
print(f"Foram um total de {qtd_homens} homens cadastrados.")
print(f"Foram um total {mulheres_idade_menos_18_anos} mulheres cadastradas com menos de 18 anos.")


