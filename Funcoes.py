# def somar(numero1, numero2):
#     '''
#     Essa funcao recebe DOIS numeros e mostra a soma deles
#     '''
    
#     return numero1 + numero2


# a = input('Deseja somar 20 com 30 ? (s/n) ')
# if a == 's':
#     somar(20,30)
# else:
#     print('Beijinhos Carol')

# num1 = int(input('Digite o primeiro número para somar: '))
# num2 = int(input('Digite o segundo número para somar: '))

# print(f'A soma é: {somar(num1,num2)}')

# help(somar)

def area(b,h):
    return b*h

a = input('Gostaria de saber a área de um retângulo? ')
if a == 's':
    b = int(input('Informe a base: '))
    h = int(input('Informe a altura: '))
    print(f'A área é: {area(b,h)} u.m. ²')
