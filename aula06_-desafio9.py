numero = int(input("Digite um número para ver sua tabela de multiplicação: "))

# Exibe a tabela de multiplicação de 1 a 10
print(f"Tabela de multiplicação do número {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")