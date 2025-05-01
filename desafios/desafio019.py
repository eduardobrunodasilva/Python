from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador sortear o número
print('_=_' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('_=_' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tente advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
