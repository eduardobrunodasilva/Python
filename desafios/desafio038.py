'''Melhore o jogo do desafio 019, onde o computador vai
pensar em um número de 0 a 10. só que agora o jogador
vai tentar advinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer'''

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas'.format(palpites))