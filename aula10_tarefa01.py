# criando uma matriz 3x3
"""
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 

print("elemento(0,0):", matriz[0][0])#saida 1 
print("elemento(2,1):", matriz[2][1])#saida 8   

for linha in matriz:
    for elemento in linha:
        print(f"|{elemento}|",end='')    
    print()  

     

matriz = []
for i in range(4):
    linha=[]
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]:"))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)

"""
matriz_4_4=[
   [1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]
] 


def soma_dos_elementos():
    soma=0
    for i in range(4):
        for j in range(4):
            soma=soma + matriz_4_4[i][j]
    print(f"soma dos elementos acima da diagonal principal: {soma}") 


def soma_dos_elementos_v2():
    soma=0
    for linha in matriz_4_4:
        soma=soma+sum(linha)
    print(f"soma dos elementos acima da diagonal principal: {soma}")     




def soma_dos_elementos_v3():
    soma=0
    for i in range(4):
        soma=soma+sum(matriz_4_4[i])
    print(f"soma dos elementos acima da diagonal principal: {soma}") 



#atividade 01.4
def maior_valor_de_cada_linha():
    for i, linha in enumerate(matriz_4_4):
        print(f"maior valor da linha {i}: {max(linha)}")
        maior=matriz_4_4[i][0]
        for j in range(4):
            if matriz_4_4[i][j]> maior:
                maior = matriz_4_4[i][j]
    print(f"Maior valor da linha {i}:{maior}")        

print(f"\n\n")

def contagem_pares():
    impares=0
    pares = 0
    vet_pares=[]
    vet_impares=[]
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                pares= pares +1
                vet_pares.append(matriz_4_4[i][j])
            else:
                impares = impares + 1
                vet_impares.append (matriz_4_4[i][j])    
    print(f"Quantidade de numeros pares:{pares}")    
    print(f"Quantidade de numeros impares:{impares}")

    print(f"os numeros pares são :{vet_pares}")
    print(f"os numeros impares são :{vet_impares}")

num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

for j in range(4):
    matriz[linha_escolhida][j] *= num

for linha in matriz:
    print(linha)
















if __name__== "__main__":
    #soma_dos_elementos()
    #soma_dos_elementos_v2()
    #soma_dos_elementos_v3()
    #maior_valor_de_cada_linha()
    contagem_pares()






