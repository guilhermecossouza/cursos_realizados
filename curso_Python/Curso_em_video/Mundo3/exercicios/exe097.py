def mensagem(msg):
    tamanho_linha = len(msg) + 4
    print("~" * tamanho_linha)
    print(f"  {msg}")
    print("~" * tamanho_linha)


# programa principal

mens = str(input("Digite sua mensagem: ")).strip()
mensagem(mens)