from random import randint
from time import sleep

def gerar_jogo():
    jogo = []
    pares = []
    impares = []

    while len(pares) < 3:
        num = randint(1, 60)
        if num % 2 == 0 and num not in pares and num not in impares:
            pares.append(num)

    while len(impares) < 3:
        num = randint(1, 60)
        if num % 2 != 0 and num not in pares and num not in impares:
            impares.append(num)

    jogo = pares + impares
    jogo.sort()
    return jogo

print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = []
for _ in range(quant):
    jogos.append(gerar_jogo())

print('-' * 3, f'SORTEANDO {quant} JOGOS', '-' * 3)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    sleep(1)
print('-' * 5, '< BOA SORTE! >', '-' * 5)