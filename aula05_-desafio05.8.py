# Solicita a idade do usuário
idade = int(input("Qual é a sua idade? "))

# Solicita informação sobre a carteira de motorista
possui_carteira = input("Você possui carteira de motorista? (s/n): ").lower()

# Verifica as condições para dirigir
if idade >= 18 and possui_carteira == 's':
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")