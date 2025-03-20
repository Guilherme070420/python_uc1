nome = ""
while nome != "sair":
    nome = input("Digite seu nome (ou 'sair' para encerrar): ").lower()
    if nome != "sair":
        print(f"Olá, {nome.capitalize()}!")
print("Encerrando o programa.")