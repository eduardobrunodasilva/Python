from random import randint, choice
from time import sleep

mais_sorteados = [5, 10, 23, 33, 42, 53, 27, 8, 30, 47]
menos_sorteados = [3, 14, 21, 36, 44, 60, 2, 18, 39, 49]


blocos = {
    1: list(range(1, 16)),
    2: list(range(16, 31)),
    3: list(range(31, 46)),
    4: list(range(46, 61))
}

def gerar_jogo():
    jogo = set()
    pares = set()
    impares = set()


    combinacoes = [(3, 3), (4, 2), (2, 4)]
    num_pares, num_impares = choice(combinacoes)


    numeros_possiveis = []
    for bloco in blocos.values():
        numeros_possiveis.append(choice(bloco))


    while len(numeros_possiveis) < 6:
        if randint(0, 1):
            candidato = choice(mais_sorteados)
        else:
            candidato = choice(menos_sorteados)
        if candidato not in numeros_possiveis:
            numeros_possiveis.append(candidato)


    for num in numeros_possiveis:
        if num % 2 == 0 and len(pares) < num_pares:
            pares.add(num)
        elif num % 2 != 0 and len(impares) < num_impares:
            impares.add(num)


    while len(pares) < num_pares:
        num = randint(1, 60)
        if num % 2 == 0 and num not in pares and num not in impares:
            pares.add(num)
    while len(impares) < num_impares:
        num = randint(1, 60)
        if num % 2 != 0 and num not in pares and num not in impares:
            impares.add(num)

    jogo = list(pares.union(impares))
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
