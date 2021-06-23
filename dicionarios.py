# vingadores = {
#     'Chris Evans' : 'Capitão América',
#     'Mark Ruffalo' : 'Hulk',
#     'Tom Hiddleston' : 'Loki',
#     'Chris Hemworth' : 'Thor',
#     'Robert Downey Jr' : 'Homem de Ferro',
#     'Scarlett Johansson' : 'Viúva Negra'
# }

# vingadores['homem-formiga'] = 'Paul Rudd'
# print(vingadores)

# continuar = 'S'
# notas_alunos = {}
# while continuar == 'S':
#     aluno = input('Nome do Aluno: ')
#     nota = int(input('Informe a nota do aluno: '))
#     notas_alunos[aluno] = nota
#     continuar = input('Deseja continuar? (S/N ').upper()
# print(notas_alunos)



# numeros = {}
# while len(numeros)<6:
#     numero = int(input('Digite um número: '))
#     quadrado = numero**2
#     numeros[numero] = quadrado
    
# print(numeros)


# numeros = {}
# for i in range(1,11):
#     numeros[i] = i**2
# print(numeros)


#Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

#Ex.: Feira = {'Tomate': 10, 'Abacate': 15, 'Cebola' : 0, 'Batata': 12}





#--------------------------------------------------------------------------------------------------------



# 1.Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

# continuar = 'S'
# notas_alunos = {}
# # situação = {}
# while continuar == 'S':
#     Dicionario = []
#     aluno = input('Nome do Aluno: ')
#     nota = float(input('Informe a nota do aluno: '))
#     # notas_alunos[aluno] = nota
#     Dicionario.append(nota)
    
    
#     if Dicionario[0] >= 7:
#         Dicionario.append('Aprovado')
      
     
        
#     elif Dicionario[0] >= 5:
#        Dicionario.append('Recuperação')
                
#     else:
#         Dicionario.append('Reprovado')
        
#     notas_alunos[aluno] = Dicionario
                   
#     continuar = input('Deseja continuar? (S/N) ').upper()
    
    
# print(notas_alunos)
    
# --------------------------------Solução Marcelo da Rocha------------------------------------------

# aluno = dict()
# aluno['Nome'] = str(input('Nome: '))
# aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

# if aluno['Média'] >= 7:
#      aluno['situação'] = 'Aprovado'
#      print('Aluno está APROVADO')
# elif 5<= aluno['Média'] < 7:  	# aqui eu quero colocar entre 6 e 7
#      aluno['situação'] = 'Recuperação' 
#      print('Aluno em RECUPERAÇÃO')
# else: 
#      aluno['situação'] = 'Reprovado'
#      print('Aluno em REPROVADO')


#------------------------------Resolvido-----------------------




# 2.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


# Trabalhador = {}
# continuar = 'S'
# while continuar == 'S':
#     nome = input('Nome do Trabalhador: ')
#     nasci = int(input('Informe o ano de nascimento: '))
#     Ctps = input('Informe o ano do primero trabalho com a carteira assinada: ')
    
#     Trabalhador[nome] = nasci, Ctps
#     print(Trabalhador[Ctps])
#      if Ctps != 0:
         
#     # print(Trabalhador)
        
    

#     continuar = input('Deseja continuar? (S/N) ').upper()

#---------------------------------------Resolução do Cauã---------------------------


# Dicionario = {}
# Lista = []

# nome = input("Diga seu nome: ")
# ano = int(input("Diga o ano que você nasceu: "))
# idade = 2021 - ano
# trab = int(input("Diga o ano do seu primeiro trabalho, se não tiver coloque 0: "))
# trabalhado = 2021-trab
# aposentadoria = (35-trabalhado) + idade

# Lista.append(nome)
# Lista.append(ano)
# Lista.append(idade)
# Lista.append(trab)
# Lista.append(trabalhado)
# Lista.append(aposentadoria)

# Dicionario['Nome'] = Lista[0]
# Dicionario['Ano de Nascimento'] = Lista[1]
# Dicionario['Idade'] = Lista[2]
# Dicionario['Ano que começou a trabalhar'] = Lista[3]
# Dicionario['Anos trabalhados'] = Lista[4]
# Dicionario['Idade que se aposentará'] = Lista[5]


# print(Dicionario)



#-----------------------------------------Solução do Caua-----------------------------------

# lista = {}
# lista2 = []

# nome = input("Diga seu nome: ").capitalize()
# ano = int(input("Diga o ano que você nasceu: "))
# idade = 2021 - ano
# trab = int(input("Diga o ano do seu primeiro trabalho, se não tiver coloque 0: "))
# contrib = 2021 - trab
# aposent = (35 - contrib) + idade

# lista2.append(f"O ano que você nasceu: {ano}")
# lista2.append(f"Sua idade: {idade}")
# lista2.append(f"Você vai se aposentar com {aposent} anos ")
# if trab != 0:
#     sal = float(input("Diga o seu salário: "))
#     lista2.append(f"Salário: R${sal}")
#     lista2.append(f"O primeiro ano de contratação é: {trab}")
# if trab == 0 :
#     lista2.append(f"Você nunca trabalhou")



# lista[nome] = lista2
# print(lista)






# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma Dicionario. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma Dicionario com as mulheres.
# D) Uma Dicionario com as idades que estão acima da média.
# OBS: O programa deve garantir


#------------------------------------------------Solução do Marcelo---------------------------------------


# lista = list()
# mulheres = list()
# dicionario = dict()
# soma = 0

# while True:
#     dicionario.clear()
#     dicionario['Nome'] = str(input('Nome: ')).strip()
#     dicionario['Idade'] = int(input('Idade: '))

#     while True:
#         dicionario['Sexo:'] = str(input('Sexo: [M/F]')).strip().upper()[0]
#         if dicionario['Sexo:'] in 'MF':
#             break
#         print('Opção Inválida! Tente novamente, desta vez com M ou F.')

#     lista.append(dicionario.copy())
#     soma += dicionario['Idade']

#     if dicionario['Sexo:'] == 'F':
#         mulheres.append(dicionario['Nome'])

#     while True:
#         op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#         if op in 'SN':
#             break
#     if op == 'N':
#         break


# print(f'''A) Total de pessoas cadastradas: {len(lista)}
# B) Média de idade: {soma/len(lista):.2f}
# C) Mulheres cadastradas {mulheres}
# D) Pessoas com idade acima da média: ''')

# for a in lista:
#     if a['Idade'] >= soma/len(lista):
#         print(f'     {a["Nome"]}: {a["Idade"]}')

#----------------------------------------------------------------------------------------

# Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve 
# receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só.

dicionario = {'Aluno': 'Rudhy', 'Idade': 30, 'Média': 9.9}

for i in dicionario:
    print(i)
    dicionario[i] = input('Digite o novo valor: ')
    
print(dicionario)