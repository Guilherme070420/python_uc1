soma = 0

# Loop para solicitar números
while True:
    numero = int(input("Digite um número (negativo para encerrar): "))
    if numero < 0:
        break  # Encerra o loop quando um número negativo for digitado
    soma += numero  # Adiciona o número positivo à soma

# Exibe o resultado
print(f"A soma dos números positivos é: {soma}")