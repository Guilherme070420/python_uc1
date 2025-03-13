# Solicita a idade do usuário
idade = int(input("Qual é a sua idade? "))

# Verifica as condições de viagem
if idade >= 18:
    print("Você pode viajar sozinho.")
elif 16 <= idade <= 17:
    autorizacao = input("Você tem autorização dos seus pais? (s/n): ").lower()
    if autorizacao == 's':
        print("Você pode viajar com a autorização dos seus pais.")
    else:
        print("Você não pode viajar sem a autorização dos seus pais.")
else:
    print("Você não pode viajar sozinho.")