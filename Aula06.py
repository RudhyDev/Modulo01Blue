#Exemplo de While

# senha = 'Blue123'

# entrada = input('Digite sua senha: ')
# erros = 0
# while senha != entrada:
#     erros += 1
#     entrada = input('Senha incorreta! \n Digite novamente: ')
#     if entrada == senha:
#         print('Bem vindo')
#     if erros == 5:
#         print('Tentativas esgotadas!')
#         break

#For exemplo

a = "Ola Glaeraaa"
letra_a = 0
print(len(a))
print()
for i in a:
    print(i)
    if i == 'a' or i =='A':
        letra_a += 1
        print('Olha o A aí!')
        
