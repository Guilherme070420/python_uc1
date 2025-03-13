# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    par_ou_impar = "par"
else:
    par_ou_impar = "ímpar"

# Verifica se o número é positivo ou negativo
if numero > 0:
    positivo_ou_negativo = "positivo"
elif numero < 0:
    positivo_ou_negativo = "negativo"
else:
    positivo_ou_negativo = "neutro"  # Para o caso específico do zero

# Exibe os resultados
print(f"O número {numero} é {par_ou_impar} e {positivo_ou_negativo}.")