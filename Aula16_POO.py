# class Mamifero():
#     #criando o método construtor, ele vai servir para passar todos os atributos para os objetos que eu for criando
#     def __init__(self, nome, pelo, cor, tamanho, idade): # esse construtor possui 4 atributos
#         self.nome = nome
#         self.pelo = pelo
#         self.cor = cor
#         self.tamanho = tamanho
#         self.idade = idade
        
#     def crescer(self, anos):
#         self.idade += anos
        
#     def locomover(self):
#         print('O mamífero está andando')
    
#     def comer(self):
#         self.tamanho = 'grande'
        
# cachorro = Mamifero('Eddie', 'curto', 'preto', 'pequeno', 2)
# cachorro.crescer(5)
# cachorro.locomover()
# cachorro.comer()

# print(vars(cachorro))

#---------------------------------------------------------------------------------------------------

# 1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos.

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def dados(self):
        # print(f'Nome completo: {self.nome} {self.sobrenome}\n idade: {self.idade}')
        return [self.nome, self.sobrenome, self.idade]
        
        
        
gustavo = Pessoa('Gustavo', 'Batata', 27)
lista = gustavo.getdados() #não sei porque não está funcionando
print(lista)