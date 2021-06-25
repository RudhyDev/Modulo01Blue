# 1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# def soma (a, b, c):
#     return a + b + c

# print(soma(3,5,9))

#-----------------------------------------------------------------------------------------------------

# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

# def valor(n):
#     if n == 0:
#         return '0'
#     elif n >0:
#         return 'P'
#     else:
#         return 'N'
    
# print(valor(45))

#-----------------------------------------------------------------------------------------------------

# 3.Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

# def somaImposto(taxaImposto, custo):
#     return custo*(1+taxaImposto/100)
    
# imposto = int(input('Digite a porcentagem de imposto que incidirá no custo (valor inteiro): '))    
# custo = int(input('Informe qual é o valor que receberá o imposto: '))

# print(f'O valor final com o imposto é: {somaImposto(imposto, custo)}')

#-----------------------------------------------------------------------------------------------------

# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

# def salario(horas, val_hora):
#     if horas > 40:
#         return horas*val_hora + (horas-40)*val_hora*1.5
#     else:
#         return horas*val_hora
    
# print(salario(60,20))

#-----------------------------------------------------------------------------------------------------

# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

# def IMC(peso, altura):
#     return peso/(altura**2)

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite a sua altura'))

# print(f'O seu IMC é: {IMC(peso,altura):.2f}')

#-----------------------------------------------------------------------------------------------------

# 6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F


# def nota(n):
#     if n>= 9:
#         return 'A'
#     elif n>= 8:
#         return 'B'
#     elif n>= 7:
#         return 'C'
#     elif n>= 6:
#         return 'D'
#     else:
#         return 'F'

# n = input('Digite a sua nota: ').replace(',','.')
# n = float(n)
# print(f'Baseado na sua nota o seu conceito é: {nota(n)}')

#-----------------------------------------------------------------------------------------------------

# 7.Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

# def menor(a,b):
#     return min(a,b)

# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))

# print(f'O menor valor digitado é: {menor(a,b)}')

#-----------------------------------------------------------------------------------------------------

# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bissexto, sendo que nesses casos Fevereiro terá 29 dias.

data = input('Informe uma data no formato dd/mm/aaaa: ')
mes = str(data[3:5])

mesPorExtenso = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril', '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto', '09':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}

