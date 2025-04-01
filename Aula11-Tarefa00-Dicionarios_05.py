#definindo uma classe chamada 'carro'
class Carro:
    #metodo construtor (_init_) para inicializar os atributos
    def __init__(self,marca,modelo,ano):
        self.marca = marca #atributo
        self.modelo = modelo #atributo
        self.ano = ano #atributo
        self.ligado =False #atributo com valor padrão 


    def ligar(self):
        self.ligado = True
        print(f" o carro esta ligado")

    def desligar  (self):
        self.ligado = False
        print(f"o carro esta desligado")

    def exibir_info(self):
       
        if self.ligado == True:
            status = "ligado"
        else:
            status = "desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}")



if __name__== "__main__":
    #criando um objeto da classe carro
    print (f"criando um objeto da classe carros")
    #meu_carro = Carro("toyota", "corolla",2020)
    #print(meu_carro)

    #metodo para exibir informações do carro
    



    #criando um objeto da classe carro
    print (f" criando um objeto da classe de carros")
    golzinho_velho = Carro("WV","Gol",2024)
    golzinho_velho.exibir_info()