aluno_1 = {"nome": "gui", "notas":[10,7,8,7]}

aluno_2 = {"nome":  "renan","notas":[7, 6, 9, 10]}

aluno_3 = {"nome":"jorge","notas": [5, 6, 7, 6]}

print(f"dados do aluno 1 {aluno_1}")

print(f'as notas do aluno {aluno_1["nome"]}são {aluno_1["notas"]}')

media = sum (aluno_1["notas"])/len (aluno_1["notas"])
print(f'o aluno {aluno_1["nome"]} obteve media igual a:{media}')

aluno_1["media"]=media
print (f"dados do aluno 1 {aluno_1}")