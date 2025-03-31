
#criar dicionario
pessoas={"nome": "papagaio", "idade" :49, "cidade":"Petropolis"}
print(f"Dados da pessoa:{pessoas}")

pessoas["idade"]=48
print(f"Dados atualizado: {pessoas}")

pessoas["email"]="gmail.com"
print(f"dados atualizado:{pessoas}")

pessoas["sexo"]="m"
print(f"Dados atualizados:{pessoas}")

#exercicio 2

d1={"a":1,"b":2}
d2={"b":3,"c":4}
d3={**d1, **d2}
print(f"resultado",d1)

d3=d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}

print("dicionarios originais")
print(f"d1 : {d1}")
print(f"d2  :{d2}")

d1.update(d2)
d2.update(d3)

print(f"dicionarios atualizados")
print(f"d1   :{d1}")
print(f"d2   :{d2}")

