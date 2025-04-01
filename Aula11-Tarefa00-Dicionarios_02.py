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
