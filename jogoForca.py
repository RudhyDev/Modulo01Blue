# Faça um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.
from random import choice

palavras = ['arroz', 'batata', 'aspas', 'lista', 'nebuloso']

quantidade_erros_atual = 0

quantidade_erros_jogo = 6 #quando errar pela sesta vez perde o jogo

letras_erradas = []

letras_certas = []

palavra = choice(palavras).lower()
palavra_exibicao = list('_'*len(palavra))

print('Bem-vindo ao jogo da forca')
print(f'Voce pode cometer até {quantidade_erros_jogo-1} erros, ou seja, no erro número {quantidade_erros_jogo} você perde o jogo')
print('Boa sorte XD')
print()

while quantidade_erros_atual < quantidade_erros_jogo and '_' in palavra_exibicao:
    print('Palavra: ', ' '.join(palavra_exibicao))
    print(f'Status: {quantidade_erros_atual} de {quantidade_erros_jogo} erros')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    letra = input('Digite uma letra: ').lower()
    
    while letra in letras_erradas or letra in letras_certas:
        letra = input(f'A letra >>> {letra} <<< já foi utilizada, por favor informe outra letra').lower()
    print()
    
    if letra not in palavra:
        letras_erradas.append(letra)
        quantidade_erros_atual += 1
    else:
        letras_certas.append(letra)
        indice = 0
        while indice < len(palavra):
            if palavra[indice] == letra:
                palavra_exibicao[indice] = letra
            indice += 1
    
if '_' not in palavra_exibicao:
    print(f'Parabéns você ganhou o jogo!!!')
    
if quantidade_erros_atual == quantidade_erros_jogo:
    print(f'Você acaba de ser enforcado')