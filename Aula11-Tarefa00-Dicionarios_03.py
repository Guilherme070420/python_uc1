frase ="o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}
palavras_2={"não","existe","nenhuma","comida","azul","existe" }

for palavra in palavras:
    contagem[palavras]=contagem.get(palavra,0) + 1
print(contagem)
