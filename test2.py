class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#Crie um método para retornar as informações formatas com Nome e Idade: 
    def __str__(self):
        return f"{', '.join([f'{chave.capitalize()}: {valor}' for chave, valor in self.__dict__.items()])}"
      
        
    
    

# Entrada do usuário
nome = input()
idade = int(input())

# Crie uma instância da pessoa:
p1 = Pessoa(nome, idade)

#Chame o método para retornar as informações formatadas e imprima o resultado:
print(p1)