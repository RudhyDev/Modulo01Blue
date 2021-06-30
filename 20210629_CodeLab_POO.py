# # Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

# import random

# class Moedas():
#     def __init__(self):
#         self.lado = 'cara'
        
    
    
#     def lancar(self):
#         if random.randint(0,1) == 0:
#             self.lado = 'Cara'
#         else:
#             self.lado = 'coroa'
#         return self.lado
    

    
# class Dados():
#     def __init__(self):
#         self.lado = 1
    
#     def lancar(self):
#         return random.randint(1,6) 

# moeda = Moedas()    
# dado = Dados()
# op = 1


# while True:
#     op = int(input('0.Sair \n'
#                    '1.Lançar a moeda: \n'
#                    '2.Lançar o dados: '))
    
#     if op==1:
#         print('Moeda: ', moeda.lancar())
#     elif op == 2:
#         print('O número que saiu foi: ', dado.lancar())
#     else:
#         break
  
#------------------------------------------------------------------------------  
